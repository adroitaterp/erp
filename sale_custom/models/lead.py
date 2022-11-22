

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

    # @api.onchange('user_id')
    # def onchange_user_id(self):
    #     if self.user_id:
    #         template_id = self.env.ref('sale_custom.email_crm_assign').id
    #         template = self.env['mail.template'].browse(template_id)
    #         template.send_mail(self.id, force_send=True)

