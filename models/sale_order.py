# -*- coding: utf-8 -*-
from odoo import api, models
from odoo.tools.translate import _


class SaleOrder(models.Model):
    """Extend sale order to add surcharge line on payment term change."""

    _inherit = "sale.order"

    @api.onchange("payment_term_id")
    def _onchange_payment_term_id(self):
        """Add or update surcharge line based on payment term (pre-save preview)."""
        # Always remove existing surcharge lines first for clean preview
        self.order_line = self.order_line.filtered(lambda line: not line.is_surcharge)

        if not self.payment_term_id:
            return

        surcharge_perc = self.payment_term_id.surcharge_percentage
        surcharge_prod = self.payment_term_id.surcharge_product_id

        if not surcharge_prod or surcharge_perc <= 0:
            return

        # Calculate subtotal excluding surcharges
        subtotal = sum(line.price_subtotal for line in self.order_line)

        surcharge_amount = subtotal * (surcharge_perc / 100)

        # Add new surcharge line in memory (taxes will be computed from product)
        self.order_line += self.env["sale.order.line"].new(
            {
                "product_id": surcharge_prod.id,
                "name": _("Surcharge for payment term: %s%%") % surcharge_perc,
                "product_uom_qty": 1,
                "price_unit": surcharge_amount,
                "is_surcharge": True,
            }
        )

    def write(self, vals):
        """Override write to ensure surcharge consistency post-save."""
        if self.env.context.get("skip_surcharge_update"):
            return super(SaleOrder, self).write(vals)

        res = super(SaleOrder, self).write(vals)

        for order in self:
            # Reload record for fresh data post-write
            order = order.browse(order.id)

            # Remove existing surcharge lines post-save
            surcharge_lines = order.order_line.filtered(lambda line: line.is_surcharge)
            if surcharge_lines:
                surcharge_lines.with_context(skip_surcharge_update=True).unlink()

            if not order.payment_term_id:
                continue

            surcharge_perc = order.payment_term_id.surcharge_percentage
            surcharge_prod = order.payment_term_id.surcharge_product_id

            if not surcharge_prod or surcharge_perc <= 0:
                continue

            # Calculate subtotal excluding old surcharges
            subtotal = sum(line.price_subtotal for line in order.order_line)

            surcharge_amount = subtotal * (surcharge_perc / 100)

            # Create persistent surcharge line (taxes from product)
            order.env["sale.order.line"].with_context(
                skip_surcharge_update=True
            ).create(
                {
                    "order_id": order.id,
                    "product_id": surcharge_prod.id,
                    "name": _("Surcharge for payment term: %s%%") % surcharge_perc,
                    "product_uom_qty": 1,
                    "price_unit": surcharge_amount,
                    "is_surcharge": True,
                }
            )

        return res
