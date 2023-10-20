from odoo import api, fields, models, _
from odoo.exceptions import ValidationError
from datetime import datetime
import logging
_logger = logging.getLogger(__name__)


class ProjectType(models.Model):
    _name = 'project.type'

    name = fields.Char(string="Type Name")
class ProjectProject(models.Model):
    _inherit = 'project.project'
    project_type_id = fields.Many2one('project.type', string="Project Type")
    
    @api.onchange('department_project_id')
    def branch_filter(self):
        aa=self.department_project_id.project_by_id
        all=[]
        for j in aa:
            all.append(j.id)
        if all:
           
            return {'domain': {'project_type_id': [('id', 'in', all)]}}
        else:
         
            return {'domain': {'project_type_id': [('id', 'in', [])]}}

       

        # if all:
        #     return {'domain': {'project_type_id':[('id','in',[all])]}}
        # else:
        #     return {'domain': {'project_type_id':[('id','in',[])]}}
            



class ProjectTask(models.Model):
    _inherit = 'project.task'

    project_type_id = fields.Many2one('project.type', string="Project Type" , related='project_id.project_type_id')

