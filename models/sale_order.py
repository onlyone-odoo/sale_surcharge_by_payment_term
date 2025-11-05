# -*- coding: utf-8 -*-
from odoo import api, models
from odoo.tools.translate import _


class SaleOrder(models.Model):
    """Extend sale order to add surcharge line on payment term change."""

    _inherit = "sale.order"

    @api.onchange("payment_term_id")
    def _onchange_payment_term_id(self):
        """Add or update surcharge line based on payment term."""
        if not self.payment_term_id:
            return

        # First, remove any existing surcharge lines
        self.order_line = self.order_line.filtered(lambda line: not line.is_surcharge)

        surcharge_perc = self.payment_term_id.surcharge_percentage
        surcharge_prod = self.payment_term_id.surcharge_product_id

        if not surcharge_prod or surcharge_perc <= 0:
            return

        # Calculate subtotal (now excluding surcharges since we filtered them)
        subtotal = sum(line.price_subtotal for line in self.order_line)

        surcharge_amount = subtotal * (surcharge_perc / 100)

        # Add new surcharge line
        self.order_line += self.env["sale.order.line"].new(
            {
                "product_id": surcharge_prod.id,
                "name": _("Surcharge for payment term: %s%%") % surcharge_perc,
                "product_uom_qty": 1,
                "price_unit": surcharge_amount,
                "tax_id": False,  # Assuming no taxes on surcharge, adjust if needed
                "is_surcharge": True,
            }
        )
