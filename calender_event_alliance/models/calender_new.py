from odoo.exceptions import Warning
from datetime import datetime
from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError
from odoo.tools import float_is_zero, float_compare
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT


class CalendarEventInheritNew(models.Model):
    _inherit = 'calendar.event'
    sent_email = fields.Selection([
        ('yes', 'Yes'),
        ('no', 'No'),
       
    ],default='',string='Are u Sending Email')
   

