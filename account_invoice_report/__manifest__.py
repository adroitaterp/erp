# -*- coding: utf-8 -*-
{
    'name': "Account Invoice Report",

    'summary': """
    Accounting invoice report
        """,

    'description': """
        Accounting invoice report
    """,

    'author': "Hamayun Fazal",
    'website': "http://www.hamayunfazal.com",

    'category': 'Uncategorized',
    'version': '0.10',

    'depends': ['base','account'],

    'data': [
        # 'security/ir.model.access.csv',
        'reports/header_fotter.xml',
        # 'reports/report.xml',
        'reports/tax_invoice_report.xml',
        'views/views.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
}
