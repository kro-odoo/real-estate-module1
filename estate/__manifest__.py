# -*- coding: utf-8 -*-
{
    'name': "estate",
    'version':'1.0',
    'summary': "Real Estate advertisements",
    'category':'Real Estate/Brokerage',
    'depends':['base', 'mail'],
    'data':[
        'security/ir.model.access.csv',
        'views/estate_property_views.xml',
        'views/estate_menus.xml',
    ],
    'demo': [],
    'application':True,
}
