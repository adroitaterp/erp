# from odoo import models, fields, api
#
#
# class CrmLead(models.Model):
#     _inherit = 'crm.lead'
#
#     email_cc = fields.Char('Cc')
#
#     # @api.multi
#     def action_send_email(self):
#         self.ensure_one()
#         template = self.env.ref('mail.template_data_leads_send_email', False)
#         compose_form = self.env.ref('mail.email_compose_message_wizard_form', False)
#         ctx = dict(
#             default_model='crm.lead',
#             default_res_id=self.id,
#             default_use_template=bool(template),
#             default_template_id=template.id,
#             default_composition_mode='comment',
#             mark_lead_as_done=self.mark_as_done,
#             email_cc=self.email_cc, # Add CC address to the email context
#         )
#         return {
#             'name': 'Compose Email',
#             'type': 'ir.actions.act_window',
#             'view_type': 'form',
#             'view_mode': 'form',
#             'res_model': 'mail.compose.message',
#             'views': [(compose_form.id, 'form')],
#             'view_id': compose_form.id,
#             'target': 'new',
#             'context': ctx,
#         }
