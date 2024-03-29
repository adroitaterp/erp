# -*- coding: utf-8 -*-
{
    'name': "Sale Custom",

    'summary': """
        Sale Custom""",

    'description': """
        Sale Custom
    """,
    
    'author': "Hamayun Fazal",
    'website': "http://www.projective.com",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'sale',
    'version': '15.0.0.24',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale_management', 'crm' ,'sale' ,'hr', 'job_estimate','sale_project'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        'data/data_sale.xml',
        'views/lead_views.xml',
        'views/sale_views.xml',
         'views/sale_views_new.xml',
       
        'views/partner_views.xml',
        'views/sale_views_inherit.xml',
        'reports/sale_proposal_report.xml',
        'reports/custom_header_footer.xml',
        'reports/sale_proposal_template.xml',
        'reports/sale_contract_template.xml',
    ],

    'installable': True,
    'auto_install': False,
    'application': False,
    'license': 'AGPL-3',
}
