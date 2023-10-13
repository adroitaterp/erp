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

    # Categories can be used to filter modules in modules listing
    # Check https://gitlab.com/flectra-hq/flectra/blob/2.0/flectra/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        # 'reports/header_fotter.xml',
        # 'reports/report.xml',
        'reports/tax_invoice_report.xml',
        # 'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
