

from odoo import models, fields, api,_
from odoo.exceptions import ValidationError , UserError


class CRMLeadInh(models.Model):
    _inherit = "crm.lead"

    @api.model
    def create(self, vals):
        res = super(CRMLeadInh, self).create(vals)
        partner = self.env['res.partner'].sudo().create({
            'name': res.name,
            'type': 'contact',
        })
        return res