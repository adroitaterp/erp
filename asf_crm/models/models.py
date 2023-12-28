from odoo import models, fields, api, Command
from collections import defaultdict

class MailActivity(models.Model):
    _inherit = 'mail.activity'

    is_done = fields.Boolean(string='Is Done', default=True)

    # def _action_done(self, feedback=False, attachment_ids=None):
    #     """ Private implementation of marking activity as done: posting a message, not deleting activity,
    #         and eventually creating the automatic next activity (depending on config).
    #         :param feedback: optional feedback from user when marking activity as done
    #         :param attachment_ids: list of ir.attachment ids to attach to the posted mail.message
    #         :returns (messages, activities) where
    #             - messages is a recordset of posted mail.message
    #             - activities is a recordset of mail.activity of forced automatically created activities
    #     """
    #     # marking as 'done'
    #     messages = self.env['mail.message']
    #     next_activities_values = []

    #     # Search for all attachments linked to the activities we are about to mark as done.
    #     attachments = self.env['ir.attachment'].search_read([
    #         ('res_model', '=', self._name),
    #         ('res_id', 'in', self.ids),
    #     ], ['id', 'res_id'])

    #     activity_attachments = defaultdict(list)
    #     for attachment in attachments:
    #         activity_id = attachment['res_id']
    #         activity_attachments[activity_id].append(attachment['id'])

    #     for activity in self:
    #         # If is_done is True, skip the unlinking
    #         if activity.is_done:
    #             continue

    #         # extract value to generate next activities
    #         if activity.chaining_type == 'trigger':
    #             vals = activity.with_context(activity_previous_deadline=activity.date_deadline)._prepare_next_activity_values()
    #             next_activities_values.append(vals)

    #         # post message on activity
    #         record = self.env[activity.res_model].browse(activity.res_id)
    #         record.message_post_with_view(
    #             'mail.message_activity_done',
    #             values={
    #                 'activity': activity,
    #                 'feedback': feedback,
    #                 'display_assignee': activity.user_id != self.env.user
    #             },
    #             subtype_id=self.env['ir.model.data']._xmlid_to_res_id('mail.mt_activities'),
    #             mail_activity_type_id=activity.activity_type_id.id,
    #             attachment_ids=[Command.link(attachment_id) for attachment_id in attachment_ids] if attachment_ids else [],
    #         )

    #         # Moving the attachments in the message
    #         activity_message = record.message_ids[0]
    #         message_attachments = self.env['ir.attachment'].browse(activity_attachments[activity.id])
    #         if message_attachments:
    #             message_attachments.write({
    #                 'res_id': activity_message.id,
    #                 'res_model': activity_message._name,
    #             })
    #             activity_message.attachment_ids = message_attachments
    #         messages |= activity_message

    #         # Set is_done to True to prevent further processing
    #         activity.write({'is_done': True})

    #     next_activities = self.env['mail.activity'].create(next_activities_values)

    #     return messages, next_activities


    


    
    def _action_done(self, feedback=False, attachment_ids=None):
        """ Private implementation of marking activity as done: posting a message, deleting activity
            (since done), and eventually create the automatical next activity (depending on config).
            :param feedback: optional feedback from user when marking activity as done
            :param attachment_ids: list of ir.attachment ids to attach to the posted mail.message
            :returns (messages, activities) where
                - messages is a recordset of posted mail.message
                - activities is a recordset of mail.activity of forced automically created activities
        """
        # marking as 'done'
        messages = self.env['mail.message']
        next_activities_values = []

        # Search for all attachments linked to the activities we are about to unlink. This way, we
        # can link them to the message posted and prevent their deletion.
        attachments = self.env['ir.attachment'].search_read([
            ('res_model', '=', self._name),
            ('res_id', 'in', self.ids),
        ], ['id', 'res_id'])

        activity_attachments = defaultdict(list)
        for attachment in attachments:
            activity_id = attachment['res_id']
            activity_attachments[activity_id].append(attachment['id'])

        for activity in self:
            # extract value to generate next activities
            if activity.chaining_type == 'trigger':
                vals = activity.with_context(activity_previous_deadline=activity.date_deadline)._prepare_next_activity_values()
                next_activities_values.append(vals)

            # post message on activity, before deleting it
            record = self.env[activity.res_model].browse(activity.res_id)
            record.message_post_with_view(
                'mail.message_activity_done',
                values={
                    'activity': activity,
                    'feedback': feedback,
                    'display_assignee': activity.user_id != self.env.user
                },
                subtype_id=self.env['ir.model.data']._xmlid_to_res_id('mail.mt_activities'),
                mail_activity_type_id=activity.activity_type_id.id,
                attachment_ids=[Command.link(attachment_id) for attachment_id in attachment_ids] if attachment_ids else [],
            )

            # Moving the attachments in the message
            # TODO: Fix void res_id on attachment when you create an activity with an image
            # directly, see route /web_editor/attachment/add
            activity_message = record.message_ids[0]
            message_attachments = self.env['ir.attachment'].browse(activity_attachments[activity.id])
            if message_attachments:
                message_attachments.write({
                    'res_id': activity_message.id,
                    'res_model': activity_message._name,
                })
                activity_message.attachment_ids = message_attachments
            messages |= activity_message

        next_activities = self.env['mail.activity'].create(next_activities_values)
        self.unlink()  # will unlink activity, dont access `self` after that
        # self.is_done=False

        return messages, next_activities





class MailMessageInh(models.Model):
    _inherit = 'mail.message'

    attendees = fields.Char()


class ActivityReportInh(models.Model):
    _inherit = "crm.activity.report"

    attendees = fields.Char()

    def _select(self):
        return super(ActivityReportInh,
                     self)._select() + ", m.attendees as attendees"

