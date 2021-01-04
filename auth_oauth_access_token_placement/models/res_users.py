# -*- coding: utf-8 -*-

import requests

from odoo import api, models


class ResUsers(models.Model):
    _inherit = 'res.users'

    @api.model
    def _auth_oauth_rpc(self, endpoint, access_token, token_location):
        if token_location == "bearer":
            return requests.get(endpoint, headers={'Authorization': 'Bearer %s' % access_token}).json()
        if token_location == "oauth":
            return requests.get(endpoint, headers={'Authorization': 'OAuth %s' % access_token}).json()
        return requests.get(endpoint, params={'access_token': access_token}).json()

    @api.model
    def _auth_oauth_validate(self, provider, access_token):
        """ return the validation data corresponding to the access token """
        oauth_provider = self.env['auth.oauth.provider'].browse(provider)
        validation = self._auth_oauth_rpc(oauth_provider.validation_endpoint, access_token, oauth_provider.access_token_location)
        if validation.get("error"):
            raise Exception(validation['error'])
        if oauth_provider.data_endpoint:
            data = self._auth_oauth_rpc(oauth_provider.data_endpoint, access_token, oauth_provider.access_token_location)
            validation.update(data)
        return validation
