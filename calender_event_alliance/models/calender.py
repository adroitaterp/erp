from odoo.exceptions import Warning
from datetime import datetime
from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError
from odoo.tools import float_is_zero, float_compare
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT




class CalendarEventInherit(models.Model):
    _inherit = 'calendar.event'
    location_id = fields.Many2one('calendar.location', string="Exact Location",required=True)

    is_done = fields.Boolean(string='Is Done', default=False)

    def mark_meeting_as_done(self):
        """Custom logic to mark the meeting as done without unlinking."""
        # Your custom logic here
        # For example, update the 'is_done' field to True
        self.write({'is_done': False})

    def unlink(self):
        for meeting in self:
            if meeting.is_done:
                raise ValueError("You cannot delete a meeting that is marked as done.")
        return super(CalendarEventInherit, self).unlink()
    
    @api.model
    def create(self, values):
        if not values.get('location_id'):
            raise ValidationError(_('Location field can not be empty'))
        if values.get('start') and values.get('stop') and values.get('location_id'):
            domain = [
                ('start', '<', values['stop']),
                ('stop', '>', values['start']),
                ('location_id', '=', values['location_id']),
            ]
            conflicting_events = self.search(domain)
            if conflicting_events:
                raise ValidationError(_('Another event is already scheduled at the same time and location!'))

        return super(CalendarEventInherit, self).create(values)

