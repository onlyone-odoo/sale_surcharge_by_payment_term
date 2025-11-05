# -*- coding: utf-8 -*-
from odoo import fields, models


class SaleOrderLine(models.Model):
    """Extend sale order line to identify surcharge lines."""

    _inherit = "sale.order.line"

    is_surcharge = fields.Boolean(
        string="Is Surcharge",
        help="Indicates if this line is a surcharge based on payment term.",
    )
