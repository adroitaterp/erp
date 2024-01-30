from odoo.exceptions import Warning
from datetime import datetime
from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError
from odoo.tools import float_is_zero, float_compare
import logging
from datetime import datetime

import logging
_logger = logging.getLogger(__name__)




class SaleOrderProjectInherit(models.Model):
    _inherit = 'sale.order'


    def open_projects_sale(self):
        raise ValidationError("You are not authorized to change stage")
        _logger.warning("jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj")
        _logger.warning("jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj")
        _logger.warning("jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj")
        _logger.warning("jjjjjjjjjjjjjBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj")
        self.ensure_one()
        view_form_id = self.env.ref('project.edit_project').id
        view_kanban_id = self.env.ref('project.view_project_kanban').id
        
        action = {
            'type': 'ir.actions.act_window',
            'domain': [('id', 'in', self.with_context(active_test=False).project_ids.ids), ('active', 'in', [True, False])],
            'view_mode': 'kanban,form',
            'name': _('Projects'),
            'context':{'create':False},
            'res_model': 'project.project',
        }
        if self.state in ['cancel']:
            action['context']={'edit':False}
        if len(self.with_context(active_test=False).project_ids) == 1:
            action.update({'views': [(view_form_id, 'form')], 'res_id': self.project_ids.id})
        else:
            action['views'] = [(view_kanban_id, 'kanban'), (view_form_id, 'form')]
        return action