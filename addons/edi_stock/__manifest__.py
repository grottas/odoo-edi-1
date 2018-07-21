# pylint: disable=missing-docstring,pointless-statement
{
    'name': "EDI for Inventory Management",
    'description': """
Electronic Data Interchange for Inventory Management
====================================================

EDI capability for the Odoo ```stock``` module.

Key Features
------------
* Create and update minimum inventory rules
* Create and update pickings from external EDI sources
* Report completed pickings to external EDI sources
    """,
    'version': '0.1',
    'depends': ['edi', 'stock'],
    'author': "Michael Brown <mbrown@fensystems.co.uk>",
    'category': "Extra Tools",
    'data': [
        'security/ir.model.access.csv',
        'views/edi_orderpoint_views.xml',
        'views/edi_orderpoint_tutorial_views.xml',
        'views/edi_move_request_views.xml',
        'views/edi_pick_request_views.xml',
        'views/edi_pick_request_tutorial_views.xml',
        'data/edi_orderpoint_data.xml',
        'data/edi_orderpoint_tutorial_data.xml',
        'data/edi_pick_request_data.xml',
        'data/edi_pick_request_tutorial_data.xml',
    ],
}