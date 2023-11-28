from odoo.exceptions import Warning
from datetime import datetime
from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError
from odoo.tools import float_is_zero, float_compare


class CalendarEventInherit(models.Model):
    _inherit = 'calendar.event'
    location = fields.Char('Location', tracking=True, required=True)
