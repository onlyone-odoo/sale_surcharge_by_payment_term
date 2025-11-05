# -*- coding: utf-8 -*-
from odoo import api, models
from odoo.tools.translate import _


class SaleOrder(models.Model):
    """Extend sale order to add surcharge line on payment term change."""

    _inherit = "sale.order"

    @api.onchange("payment_term_id")
    def _onchange_payment_term_id(self):
        """Add or update surcharge line based on payment term."""
        # Filter non-surcharge lines for subtotal calculation
        non_surcharge_lines = self.order_line.filtered(lambda l: not l.is_surcharge)
        subtotal = sum(l.price_subtotal for l in non_surcharge_lines)

        # Determine if we need to add surcharge
        add_surcharge = False
        surcharge_vals = {}
        if self.payment_term_id:
            perc = self.payment_term_id.surcharge_percentage
            prod = self.payment_term_id.surcharge_product_id
            if prod and perc > 0:
                add_surcharge = True
                surcharge_amount = subtotal * (perc / 100)
                surcharge_vals = {
                    "product_id": prod.id,
                    "name": _("Surcharge for payment term: %s%%") % perc,
                    "product_uom_qty": 1,
                    "price_unit": surcharge_amount,
                    "tax_id": False,  # Assuming no taxes on surcharge, adjust if needed
                    "is_surcharge": True,
                }

        # Build commands: unlink surcharges, keep non-surcharges
        commands = []
        for line in self.order_line:
            if line.is_surcharge:
                if line.id:  # Explicit unlink for existing lines
                    commands.append((2, line.id, 0))
                # Omit new surcharge lines (no need to unlink if no id)
            else:
                if line.id:
                    commands.append((4, line.id, 0))
                else:
                    commands.append((0, 0, line._convert_to_write(line._cache)))

        # Add new surcharge if applicable
        if add_surcharge:
            commands.append((0, 0, surcharge_vals))

        # Apply commands
        self.order_line = commands
