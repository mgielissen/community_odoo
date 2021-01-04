# -*- coding: utf-8 -*-
{
    'name': "Access Token Placement - OAuth2 Authentication",

    'summary': """Adds "Access Token Placement" selection filed to the Oauth2 provider object""",

    'description': """
Allow users to login through OAuth2 Provider.
=============================================

This module updates the original `auth_oauth` module
in order to correctly handle Oauth2 access token placement in relevant requests.


Please note that:

This is a temporary solution before the upstream issue odoo/odoo#63963 will be addressed in the Odoo.
-----------------------------------------------------------------------------------------------------

    """,

    'author': 'PluginMere',
    'website': 'https://github.com/pluginmere/community_odoo',

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Hidden/Tools',
    'license': 'LGPL-3',
    'version': '14.0.1.0.0',

    # any module necessary for this one to work correctly
    'depends': ['auth_oauth'],

    # always loaded
    'data': [
        'views/views.xml',
    ],
    'installable': True,
    'auto_install': True,
}
