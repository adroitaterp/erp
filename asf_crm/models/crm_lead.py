from odoo import models, fields, api, Command
from collections import defaultdict



class MeetingInherited(models.Model):
    _inherit = 'crm.lead'
    
    def action_sale_quotations_new(self):
        if not self.partner_id:
            return self.env["ir.actions.actions"]._for_xml_id("sale_crm.crm_quotation_partner_action")
        else:
            return self.action_new_quotation()