# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ContactAlliance(models.Model):
    _inherit = 'res.partner'

    contact_person_name = fields.Char(string="Contact Name")
    position = fields.Char(string="Position")
    contact_person_number = fields.Char(string="Contact Number")
    contact_email_address = fields.Char(string="Email Address")
    office_address = fields.Char(string="Office Address")


    name_of_accountant = fields.Char(string="Name of Accountant")
    accountant_contact_number = fields.Char(string="Accountant Contact Number")
    accountant_email_address = fields.Char(string="Accountant Email Address")

    

    



