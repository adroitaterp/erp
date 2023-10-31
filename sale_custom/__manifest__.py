# -*- coding: utf-8 -*-
{
    'name': "Sale Custom",

    'summary': """
        Sale Custom""",

    'description': """
        Sale Custom
    """,

    'author': "Musadiq Fiaz Chaudhary",
    'website': "http://www.musadiqch.com",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'sale',
    'version': '15.0.0.16',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale_management', 'crm' ,'sale' ,'hr', 'job_estimate'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        # 'data/mail_template.xml',
        'views/lead_views.xml',
        'views/sale_views.xml',
        'views/partner_views.xml',
        'reports/sale_proposal_report.xml',
        'reports/custom_header_footer.xml',
        'reports/sale_proposal_template.xml',
        'reports/sale_contract_template.xml',
    ],
    
    'license': 'LGPL-3 ',
    'installable': True,
    'auto_install': False,
    'application': False,

}
