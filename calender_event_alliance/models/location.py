from odoo.exceptions import Warning
from datetime import datetime
from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError
from odoo.tools import float_is_zero, float_compare

class LocationCalendar(models.Model):
    _name = 'calendar.location'
    name = fields.Char('Location')
    need_record = fields.Boolean(string='Needed Location', default=False)

    # @api.model 
    # def create(self, vals):
    #     if self.search_count([]) > 0:
    #         raise UserError(_('You cannot create another record'))
    #     return super(LocationCalendar, self).create(vals)
   



