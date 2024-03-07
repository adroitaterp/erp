# -*- coding: utf-8 -*-
{
    'name': "asf_crm",

    'summary': """
        """,

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'crm','sale_crm'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'security/security_groups.xml',
        'views/views.xml',
        'views/crm_views.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
    'license': 'AGPL-3',

}
