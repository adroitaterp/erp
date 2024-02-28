from odoo import api, fields, models, _
import logging
_logger = logging.getLogger(__name__)


# class ProjectProjectInherit(models.Model):
#     _inherit = 'project.project'


#     @api.model
#     def create(self, vals):
#         res = super(ProjectProjectInherit,self).create(vals)
#         template=self.env.ref('inherit_product.project_mail_pp')
#         followers = res.message_follower_ids.mapped('partner_id')
#         email_to_list = followers.mapped('email')
#         email_to_list = ', '.join(email_to_list)
#         email_values={'email_to': email_to_list}
#         template.send_mail(res.id,email_values=email_values,force_send=True)
#         return res

class ProjectProjectInherit(models.Model):
    _inherit = 'project.project'

    @api.model
    def create(self, vals):
        res = super(ProjectProjectInherit, self).create(vals)
        template = self.env.ref('inherit_product.project_mail_pp')
        followers = res.message_follower_ids.filtered(lambda follower: follower.partner_id.email)
        
        p=self.env['res.partner'].browse(vals['partner_id'])
       
        email_to_list = followers.mapped('partner_id.email')
        
        if p.email in email_to_list:
            email_to_list.remove(p.email)
        
        # Filter out any boolean values (e.g., False) from the list
        email_to_list = [email for email in email_to_list if isinstance(email, str)]
        
        email_to_list = ', '.join(email_to_list)
        email_values = {'email_to': email_to_list}
        template.send_mail(res.id, email_values=email_values, force_send=True)
        return res



    