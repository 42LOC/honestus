# -*- coding: utf-8 -*-
{
    'name': "intuit07_honestus",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Intuit07",
    'website': "https://odoo-42loc.com/",

    'category': 'Uncategorized',
    'version': '0.1',

    'depends': [
        'base',
        'product',
        'sale',
        'website'
    ],

    'data': [
        'views/portal_templates.xml',
        'views/product_views.xml',
        'views/signup_templates.xml',
        'report/sale_report_templates.xml',
    ],
}
