

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
        res.onchange_user_id_assignee()
        return res

     # def write(self, vals):
     #    res = super(CRMLeadInh, self).write(vals)
     #    for record in self:
     #        record.onchange_user_id_assignee()
     #    return res

    # @api.onchange('user_id')
    def onchange_user_id_assignee(self):
        body = 'Hello,<br/>' + 'Your Lead' + ' ' + str(self.name) + ' ' + ' ' + ' is assigned to you.<br/>' + 'Do not hesitate to contact us if you have any questions<br/><br/>' + 'Thank you<br/>' + self.env.user.name
        mail_values = {
            'subject': 'Your Lead' + ' ' + self.name,
            'body_html': body,
            'email_to': self.user_id.login,
            'email_from': self.env.user.login,
            'reply_to': self.env.user.login,
        }
        create_and_send_email = self.env['mail.mail'].create(mail_values).send()

