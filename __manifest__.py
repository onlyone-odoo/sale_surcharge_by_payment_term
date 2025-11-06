# -*- coding: utf-8 -*-
{
    "name": "Sale Surcharge by Payment Term",
    "summary": """
        Add surcharge line to sale orders based on payment term.""",
    "description": """
        This module extends payment terms to include a surcharge percentage and product.
        On changing payment term in sale order, it adds a surcharge line if applicable.
    """,
    "author": "Be OnlyOne",
    "maintainers": ["onlyone-odoo"],
    "website": "https://onlyone.odoo.com/",
    "license": "AGPL-3",
    "category": "Sales",
    "version": "17.0.2.1.0",
    "depends": ["sale", "account"],
    "data": [
        "views/account_payment_term_views.xml",
        "views/sale_order_views.xml",
    ],
    "installable": True,
    "application": False,
    "auto_install": False,
}
