# -*- coding: utf-8 -*-

from odoo import fields, models


class AuthOAuthProvider(models.Model):
    _inherit = 'auth.oauth.provider'

    access_token_location = fields.Selection([
        ('bearer', 'Bearer Authorization header'),
        ('oauth', 'OAuth Authorization header'),
        ('uri', 'URI query-string parameter (deprecated)')
        ], default='bearer', string="Access token location", required=True,
        help="Where to place Access Token when accessing provider's endpoints.")
