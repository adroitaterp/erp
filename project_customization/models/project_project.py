# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ProjectProjectInherit(models.Model):
    _inherit = "project.project"
    # department_project_id = fields.Many2one('project.department', string="Department") 
