# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Cost Analysis',
    'version': '1.0',
    'category': 'Inventory',
    'sequence': -10,
    'author': 'Julfikar-Haque-BD',
    'summary': 'Cost analysis module',
    'description': "Cost analysis module",
    'website': 'https://www.odoo.com/app',
    'depends': [
        'base',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/calculate_unit_price_views.xml',
        'views/cost_analysis_views.xml',
        'views/res_config_settings_views.xml',
        'views/expense_area_views.xml',
        'views/bank_loan.xml',
        'views/action_menu.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'OPL-1',
}