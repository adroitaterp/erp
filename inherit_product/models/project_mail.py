from odoo import api, fields, models, _


class ProjectProjectInherit(models.Model):
    _inherit = 'project.project'


    @api.model
    def create(self, vals):
        res = super(ProjectProjectInherit,self).create(vals)
        template=self.env.ref('inherit_product.project_mail_pp')
        # followers = self.message_follower_ids.filtered('email')
        # email_to_list = followers.mapped('email')
        
        template.send_mail(self.id,email_values={'email_to': self.partner_id.email},force_send=True)
        return res