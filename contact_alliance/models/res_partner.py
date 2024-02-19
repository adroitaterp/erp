# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

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
    # @api.model
    # def autocomplete(self, query, timeout=15):
       
    #     all=self.env['res.partner'].search([('name','ilike',query)])
       
    #     suggestions, _ = self.env['iap.autocomplete.api']._request_partner_autocomplete('search', {
    #         'query': query,
    #     }, timeout=timeout)
        
        
    #     if suggestions:
           
    #         results = []
    #         for suggestion in suggestions:
    #             results.append(self._format_data_company(suggestion))
           
    #         for a in all:
    #             results.append({'name':a.name ,'ignored': False})
            
    #         return results
    #     else:
    #         return []


    # @api.constrains('name')
    # def duplication_check(self):
    #     if len(self.search([('name', '=', self.name)])) > 1:
    #         raise ValidationError('Contact with this name already exists')


    @api.model
    def create(self, values):
        existing_records = self.search([('name', '=ilike', values.get('name'))])
        if existing_records:
            raise ValidationError('A record with a similar name already exists')
        return super(ContactAlliance, self).create(values)



    # @api.model
    # def name_search(self, name='', args=None, operator='ilike', limit=100):
    #     """ This method will find Customer names according to its mobile, phone, city, email, and its job position."""
    #     if name:
    #         args = args if args else []
    #         args.extend(['|', ['name', 'ilike', name]])
    #         name = ''
    #     return super(ContactAlliance, self).name_search(name=name, args=args, operator=operator, limit=limit)

