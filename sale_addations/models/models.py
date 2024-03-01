from odoo import models, fields, api
import json
import logging
_logger = logging.getLogger(__name__)


class sale_addations(models.Model):
    _inherit = 'sale.order.line'

    annual_subtotal = fields.Monetary(compute='_compute_subtotal', string='Annual Subtotal', store=True)

    @api.depends('price_subtotal','term')
    def _compute_subtotal(self):
        """
        Compute the amounts of the SO line.
        """
        for line in self:
            if line.term == 'monthly':
                line.update({
                    'annual_subtotal': line.price_subtotal*12,
                })
            elif line.term == 'quarterly':
                line.update({
                    'annual_subtotal': line.price_subtotal*4,   
                })
                

class Sale_Order_Inherit(models.Model):
    _inherit = 'sale.order'

    annual_subtotal = fields.Monetary(compute='_amount_all', string='Annual Subtotal', store=True)

    @api.depends('order_line.price_total','order_line.term')
    def _amount_all(self):
        """
        Compute the total amounts of the SO.
        """
        for order in self:
            amount_untaxed = amount_tax = annual_amount = 0.0
            for line in order.order_line:
                amount_untaxed += line.price_subtotal
                amount_tax += line.price_tax
                annual_amount += line.annual_subtotal
            order.update({
                'amount_untaxed': amount_untaxed,
                'amount_tax': amount_tax,
                'amount_total': amount_untaxed + amount_tax,
                'annual_subtotal': annual_amount
            })

    @api.depends('order_line.tax_id', 'order_line.price_unit', 'amount_total', 'amount_untaxed','order_line.term')
    def _compute_tax_totals_json(self):
        def compute_taxes(order_line):
            price = order_line.price_unit * (1 - (order_line.discount or 0.0) / 100.0)
            if order_line.term == 'monthly':
                price*=12
            elif order_line.term == 'quarterly':
                price*=4
            order = order_line.order_id
            return order_line.tax_id._origin.compute_all(price, order.currency_id, order_line.product_uom_qty, product=order_line.product_id, partner=order.partner_shipping_id)

        account_move = self.env['account.move']
        for order in self:
            tax_lines_data = account_move._prepare_tax_lines_data_for_totals_from_object(order.order_line, compute_taxes)
            total_tax_amount = sum(entry['tax_amount'] for entry in tax_lines_data if 'tax_amount' in entry)
            total= total_tax_amount + order.annual_subtotal
            
            if total > order.amount_tax:
                tax_totals = account_move._get_tax_totals(order.partner_id, tax_lines_data, total, order.annual_subtotal, order.currency_id)
            else:
                tax_totals = account_move._get_tax_totals(order.partner_id, tax_lines_data, order.amount_total, order.amount_untaxed, order.currency_id)
            order.tax_totals_json = json.dumps(tax_totals)
                


   

    

   