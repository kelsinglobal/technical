# -*-  coding: utf-8 -*-
{
    'name': 'Odoo Academy',
    'summary': """Academy app to manage Training""",
    'version': '0.1',
    'description':""" 
        Academy Module to manage Training:
        \* Courses
        \* Sessions
        \* Attendees
    """,
    'author': 'Odoo',
    'website': 'https://Odoo.com',
    'category': 'Trining',
    'depends': ['sale'],
    'data':[  
        'views/course_views.xml',
        'views/session_views.xml',
        'views/academy_menuitems.xml',
        'views/sale_views_inherit.xml',
        'security/academy_security.xml',
        'security/ir.model.access.csv',
    ],
    'demo':[ 
        'demo/academy_demo.xml',
    ],
}