# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ProjectProjectInherit(models.Model):
    _inherit = 'project.project'

    contact_person_name = fields.Char(related="partner_id.contact_person_name", string="Contact Name",readonly=False)
    position = fields.Char(related="partner_id.position", string="Job Position",readonly=False)
    contact_person_number = fields.Char(related="partner_id.contact_person_number", string="Contact Number",readonly=False)
    contact_email_address = fields.Char(related="partner_id.contact_email_address", string="Email Address",readonly=False)
    office_address = fields.Char(related="partner_id.office_address", string="Office Address",store="True",readonly=False)


    

    



