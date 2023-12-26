from odoo.exceptions import Warning
from datetime import datetime
from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError
from odoo.tools import float_is_zero, float_compare
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT




class CalendarEventInherit(models.Model):
    _inherit = 'calendar.event'
    # location = fields.Char('Location', tracking=True, required=True)
    location_id = fields.Many2one('calendar.location', string="Location")
    
    @api.model
    def create(self, values):
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