# -*- coding: utf-8 -*-

from odoo import models, fields, api
import logging
_logger = logging.getLogger(__name__)


class ProjectTaskInherit(models.Model):
    _inherit = 'project.task'
    name = fields.Char(string="Name")
   

    def action_timer_stop(self):
       
        # _logger.warning("This test relies on demo data. '%s'",values.get('follower'))
        self.action_timer_pause()
        if self.user_timer_id.timer_start and self.display_timesheet_timer:
            
            rounded_hours = self._get_rounded_hours(self.user_timer_id._get_minutes_spent())
            aa=self.user_timer_id._get_minutes_spent()
            
            
            return self._action_open_new_timesheet(aa)
        return False



class ProjectTaskCreateTimesheet(models.TransientModel):
    _inherit = 'project.task.create.timesheet'

    time_spent = fields.Float('Time',readonly=True)







   