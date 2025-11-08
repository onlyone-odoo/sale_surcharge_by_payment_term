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
    "version": "18.0.1.0.0",
    "depends": ["sale", "account"],
    "data": [
        "views/account_payment_term_views.xml",
        "views/sale_order_views.xml",
    ],
    "installable": False,
    "application": False,
    "auto_install": False,
    #ESTE ES EL MODULO DE 17 FALTA MIGRARLO
}
