from odoo import api, fields, models, _


class ProjectProjectInherit(models.Model):
    _inherit = 'project.project'


    @api.model
    def create(self, vals):
        res = super(ProjectProjectInherit,self).create(vals)
        template=self.env.ref('inherit_product.project_mail_pp')
        followers = res.message_follower_ids.mapped('partner_id')
        email_to_list = followers.mapped('email')
        email_to_list = ', '.join(email_to_list)
        email_values={'email_to': email_to_list}
        template.send_mail(res.id,email_values=email_values,force_send=True)
        return res



    