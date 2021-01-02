{
    'name': 'Captcha - Contact Form',
    'category': 'Website',
    'website': 'https://github.com/pluginmere/community_odoo',
    'license': 'AGPL-3',
    'summary': 'Captcha for Contact Form',
    'version': '14.0.1.0.0',
    'description': """
Odoo Contact Form Captcha
=========================

        """,
    'author': 'PluginMere',
    'depends': ['website_crm'],
    'external_dependencies': {'python': ['captcha']},
    'data': [
        'views/website_crm_captcha.xml',
    ],
    'installable': True,
    'auto_install': False,
}
