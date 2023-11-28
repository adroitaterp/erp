# -*- coding: utf-8 -*-
{
    'name': "Calender Event",

    'summary': """
    Add some functionlity in calender module
        """,

    'description': """
        Add some functionlity in calender module
    """,

    'author': "Hamayun Fazal ",
    'website': "http://www.projectivediv.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.3',

    # any module necessary for this one to work correctly
    'depends': ['base','calendar'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    
    'license': 'LGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
}
