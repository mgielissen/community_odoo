{
    'name': 'Captcha - Contact Form',
    'summary': 'Simple Captcha for Contact Us Form',
    'category': 'Website',
    'license': 'LGPL-3',
    'version': '14.0.1.0.0',
    'description': """
Simple Captcha for "Contact Us" Form
====================================


This module adds simple captcha to the website **Contact Us** form
in order to protect you from most of the automated bot spam.


Note
----

This module requires the `Captcha`_  Python module.

Install the dependency
~~~~~~~~~~~~~~~~~~~~~~
either with
^^^^^^^^^^^

``pip install captcha``

or with
^^^^^^^

``pip3 install captcha``


.. _Captcha: https://github.com/lepture/captcha
""",
    'author': 'PluginMere',
    'website': 'https://github.com/pluginmere/community_odoo',
    'depends': ['website_crm'],
    'external_dependencies': {'python': ['captcha']},
    'data': [
        'views/website_crm_captcha.xml',
        'views/snippets/s_website_form.xml',
    ],
    'installable': True,
    'auto_install': False,
}
