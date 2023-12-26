from odoo.exceptions import Warning
from datetime import datetime
from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError
from odoo.tools import float_is_zero, float_compare

class LocationCalender(models.Model):
    _name = 'calendar.location'
    name = fields.Char('Location')

