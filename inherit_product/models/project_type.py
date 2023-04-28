from odoo import api, fields, models, _
from odoo.exceptions import ValidationError
from datetime import datetime


class ProjectType(models.Model):
    _name = 'project.type'

    name = fields.Char(string="Type Name")


class ProjectProject(models.Model):
    _inherit = 'project.project'

    project_type_id = fields.Many2one('project.type', string="Project Type")


class ProjectTask(models.Model):
    _inherit = 'project.task'

    project_type_id = fields.Many2one('project.type', string="Project Type" , related='project_id.project_type_id')

