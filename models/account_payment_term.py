# -*- coding: utf-8 -*-
from odoo import fields, models


class AccountPaymentTerm(models.Model):
    """Extend payment terms to include surcharge options."""

    _inherit = "account.payment.term"

    surcharge_percentage = fields.Float(
        string="Surcharge Percentage",
        help="Percentage to apply as surcharge on the sale order subtotal.",
    )
    surcharge_product_id = fields.Many2one(
        "product.product",
        string="Surcharge Product",
        help="Product to use for the surcharge line in sale orders.",
    )
