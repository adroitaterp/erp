# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ProjectProjectInherit(models.Model):
    _name = 'project.department'
    name = fields.Char(string="Department")
    request_by_id = fields.Many2many('project.project', string='Project Type', store=True)
    




