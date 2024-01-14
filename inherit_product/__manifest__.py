# -*- coding: utf-8 -*-
{
    'name': "inherit_product",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.3',

    # any module necessary for this one to work correctly
    'depends': ['base', 'product', 'sale', 'mail', 'crm','project'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/project_new_department.xml',
        'views/project_type.xml',
        'views/followers.xml'
    ],
    'assets': {
        'web.assets_backend': [
        'inherit_product/static/src/js/fields.js',
        ],
        },
    'license': 'LGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
}
