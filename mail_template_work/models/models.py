# -*- coding: utf-8 -*-

from odoo import models, fields, api, _, Command
import datetime
import ast
import base64

from odoo.exceptions import UserError


# class ResUsers(models.Model):
#     _inherit = 'res.users'
#
#     is_unique = fields.Boolean('is unique')
#
#     def get_details(self):
#         template = self.env.ref('mail_template_work.crm_lead_custom_template')
#         if template:
#             p1 = """ <tr class="text-center"><h4>Active Leads for last 24 hours</h4></tr> """
#             p2 = """ <tr class="text-center"><h4>Activities for last 24 hours</h4></tr> """
#             p3 = """ <tr class="text-center"><h4>Sale Orders for last 24 hours</h4></tr> """
#             body_line = ""
#             x_body_line = ""
#             today = fields.Datetime.now() - datetime.timedelta(days=1)
#             get_user = self.env['res.users'].search([])
#             for user_id in get_user:
#                 leads = self.env['crm.lead'].search([('user_id', '=', user_id.id),('create_date', '>=', today)])
#                 if leads:
#                     count = len(leads)
#                     body_line += """<tr class="text-left"><strong><th style="font-size:18.0pt;font-family:&quot;Calibri&quot;,&quot;sans-serif&quot;;color:#67B7D1">{0}</th></strong>""".format(
#                         count) \
#                                  + """<td style="font-size:11.0pt;font-family:&quot;Calibri&quot;,&quot;sans-serif&quot;;color:#C5C5C5">{0}</td></tr>""".format(
#                         user_id.name)
#             body_line += p2
#             for user_id in get_user:
#                 counter = 0
#                 activities = self.env['crm.activity.report'].search([('user_id', '=', user_id.id),('create_date', '>=', today)])
#                 if activities:
#                     activity_type = self.env['mail.activity.type'].search([])
#                     for type in activity_type:
#                         x_activities = activities.filtered(lambda a:a.mail_activity_type_id.id == type.id)
#                         if x_activities:
#                             type_id = type.name
#                         else:
#                             type_id = "---"
#                         x_count = len(x_activities)
#                         if x_count > 0:
#                             if counter == 0:
#                                 body_line +=  """<tr class="text-left"><strong><th style="font-size:11.0pt;font-family:&quot;Calibri&quot;,&quot;sans-serif&quot;;color:#C5C5C5">{0}</th></strong>""".format(
#                                         user_id.name)
#                             if counter > 0:
#                                 body_line += """<td></td><td></td>"""
#                             body_line += """<td style="font-size:18.0pt;font-family:&quot;Calibri&quot;,&quot;sans-serif&quot;;color:#67B7D1">{0}</td>""".format(
#                                 x_count) + """ <td style="font-size:11.0pt;font-family:&quot;Calibri&quot;,&quot;sans-serif&quot;;color:#00A300">{}</td></tr>""".format(type_id)
#                             counter += 1
#             body_line += p3
#             for user_id in get_user:
#                 counter = 0
#                 sale_orders = self.env['sale.order'].search([('user_id', '=', user_id.id),('create_date', '>=', today)])
#                 states = ['to_proposal_approve','draft', 'sent', 'to_contract_approve', 'customer_approval','sale', 'done', 'cancel', 'rejected']
#                 for state in states:
#                     x_sale_order = sale_orders.filtered(lambda x:x.state == state)
#                     if x_sale_order:
#                         status = self.get_state(state)
#                     else:
#                         status = "---"
#                     x_count = len(x_sale_order)
#                     if x_count > 0:
#                         if counter == 0:
#                             body_line += """<tr class="text-left"><strong><th style="font-size:11.0pt;font-family:&quot;Calibri&quot;,&quot;sans-serif&quot;;color:#C5C5C5">{0}</th></strong>""".format(
#                                 user_id.name)
#                         if counter > 0:
#                             body_line += """<td></td><td></td>"""
#                         body_line += """<td style="font-size:18.0pt;font-family:&quot;Calibri&quot;,&quot;sans-serif&quot;;color:#67B7D1">{0}</td>""".format(
#                             x_count) + """ <td style="font-size:11.0pt;font-family:&quot;Calibri&quot;,&quot;sans-serif&quot;;color:#00A300">{}</td></tr>""".format(status)
#                         counter += 1
#             body_html = p1 + body_line
#             template.email_from = 'contact@alliance-acc.com'
#             template.body_html = body_html
#             template.subject = "Salesperson Leads and Activity Report"
#             users = get_user.filtered(lambda x: x.is_unique)
#             for user in users:
#                 template.email_to = user.login
#                 template.send_mail(user.id, force_send=True)
#                 print("====================")
#
#     def get_state(self,state):
#         if state == 'to_proposal_approve':
#             return 'Waiting For Proposal Approval'
#         if state == 'draft':
#             return 'Proposal'
#         if state == 'sent':
#             return 'Proposal Sent'
#         if state == 'to_contract_approve':
#             return 'Waiting For Contract Approval'
#         if state == 'customer_approval':
#             return 'Customer Approval'
#         if state == 'sale':
#             return 'Contract'
#         if state == 'done':
#             return 'Locked'
#         if state == 'cancel':
#             return 'Cancelled'
#         if state == 'rejected':
#             return 'Rejected'

class MailComposeMsg(models.TransientModel):
    _inherit = 'mail.compose.message'

    x_partner_ids = fields.Many2one('res.partner', string='Cc')

    def _action_send_mail(self, auto_commit=False):
        """ Process the wizard content and proceed with sending the related
            email(s), rendering any template patterns on the fly if needed. """
        notif_layout = self._context.get('custom_layout')
        # Several custom layouts make use of the model description at rendering, e.g. in the
        # 'View <document>' button. Some models are used for different business concepts, such as
        # 'purchase.order' which is used for a RFQ and and PO. To avoid confusion, we must use a
        # different wording depending on the state of the object.
        # Therefore, we can set the description in the context from the beginning to avoid falling
        # back on the regular display_name retrieved in '_notify_prepare_template_context'.
        model_description = self._context.get('model_description')
        for wizard in self:
            # Duplicate attachments linked to the email.template.
            # Indeed, basic mail.compose.message wizard duplicates attachments in mass
            # mailing mode. But in 'single post' mode, attachments of an email template
            # also have to be duplicated to avoid changing their ownership.
            if wizard.attachment_ids and wizard.composition_mode != 'mass_mail' and wizard.template_id:
                new_attachment_ids = []
                for attachment in wizard.attachment_ids:
                    if attachment in wizard.template_id.attachment_ids:
                        new_attachment_ids.append(
                            attachment.copy({'res_model': 'mail.compose.message', 'res_id': wizard.id}).id)
                    else:
                        new_attachment_ids.append(attachment.id)
                new_attachment_ids.reverse()
                wizard.write({'attachment_ids': [Command.set(new_attachment_ids)]})

            # Mass Mailing
            mass_mode = wizard.composition_mode in ('mass_mail', 'mass_post')

            ActiveModel = self.env[wizard.model] if wizard.model and hasattr(self.env[wizard.model],
                                                                             'message_post') else self.env[
                'mail.thread']
            if wizard.composition_mode == 'mass_post':
                # do not send emails directly but use the queue instead
                # add context key to avoid subscribing the author
                ActiveModel = ActiveModel.with_context(mail_notify_force_send=False, mail_create_nosubscribe=True)
            # wizard works in batch mode: [res_id] or active_ids or active_domain
            if mass_mode and wizard.use_active_domain and wizard.model:
                res_ids = self.env[wizard.model].search(ast.literal_eval(wizard.active_domain)).ids
            elif mass_mode and wizard.model and self._context.get('active_ids'):
                res_ids = self._context['active_ids']
            else:
                res_ids = [wizard.res_id]

            batch_size = int(self.env['ir.config_parameter'].sudo().get_param('mail.batch_size')) or self._batch_size
            sliced_res_ids = [res_ids[i:i + batch_size] for i in range(0, len(res_ids), batch_size)]

            if wizard.composition_mode == 'mass_mail' or wizard.is_log or (
                    wizard.composition_mode == 'mass_post' and not wizard.notify):  # log a note: subtype is False
                subtype_id = False
            elif wizard.subtype_id:
                subtype_id = wizard.subtype_id.id
            else:
                subtype_id = self.env['ir.model.data']._xmlid_to_res_id('mail.mt_comment')

            for res_ids in sliced_res_ids:
                # mass mail mode: mail are sudo-ed, as when going through get_mail_values
                # standard access rights on related records will be checked when browsing them
                # to compute mail values. If people have access to the records they have rights
                # to create lots of emails in sudo as it is consdiered as a technical model.
                batch_mails_sudo = self.env['mail.mail'].sudo()
                all_mail_values = wizard.get_mail_values(res_ids)
                partner_ids = []
                if ActiveModel._name == 'crm.lead':
                    partner_ids = []
                    num = ''
                    for val in all_mail_values:
                        num = val
                        break
                    for id in self.partner_ids.ids:
                        partner_ids.append(id)
                    if self.x_partner_ids:
                        partner_ids.append(self.x_partner_ids.id)
                    all_mail_values[num]['partner_ids'] = partner_ids
                for res_id, mail_values in all_mail_values.items():
                    if wizard.composition_mode == 'mass_mail':
                        batch_mails_sudo |= self.env['mail.mail'].sudo().create(mail_values)
                    else:
                        post_params = dict(
                            message_type=wizard.message_type,
                            subtype_id=subtype_id,
                            email_layout_xmlid=notif_layout,
                            add_sign=not bool(wizard.template_id),
                            mail_auto_delete=wizard.template_id.auto_delete if wizard.template_id else self._context.get(
                                'mail_auto_delete', True),
                            model_description=model_description)
                        post_params.update(mail_values)
                        if ActiveModel._name == 'mail.thread':
                            if wizard.model:
                                post_params['model'] = wizard.model
                                post_params['res_id'] = res_id
                            if not ActiveModel.message_notify(**post_params):
                                # if message_notify returns an empty record set, no recipients where found.
                                raise UserError(_("No recipient found."))
                        else:
                            ActiveModel.browse(res_id).message_post(**post_params)

                if wizard.composition_mode == 'mass_mail':
                    batch_mails_sudo.send(auto_commit=auto_commit)
