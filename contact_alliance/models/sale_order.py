# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SaleOrderInherit(models.Model):
    _inherit = 'sale.order'

    contact_person_name = fields.Char(related="partner_id.contact_person_name", string="Contact Name")
    position = fields.Char(related="partner_id.position", string="Job Position")
    contact_person_number = fields.Char(related="partner_id.contact_person_number", string="Contact Number")
    contact_email_address = fields.Char(related="partner_id.contact_email_address", string="Email Address")
    office_address = fields.Char(related="partner_id.office_address", string="Office Address")


    

    



