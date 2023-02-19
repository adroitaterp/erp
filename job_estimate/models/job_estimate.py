# -*- coding: utf-8 -*-

from odoo import models, fields, api

# class InheritSaleOrder(models.Model):
#     _inherit = 'sale.order'
#
#     estimation_ref = fields.Many2one('job.estimation')


class JobEstimate(models.Model):
    _name = 'job.estimate'
    _rec_name = 'estimate_name'

    estimate_name = fields.Char('Estimate', readonly=True, required=True, copy=False, default='New')
    state = fields.Selection([('draft', 'Draft'), ('confirmed', 'Confirmed'), ('quotation', 'Quotation')], default='draft')
    customer_id = fields.Many2one('res.partner')
    child_ids = fields.Many2one('res.partner', 'Contact Person')
    email = fields.Char(related='customer_id.email', string='Email')
    payment_details = fields.Char('Payment Details')
    estimate_lines = fields.One2many('job.estimate.line', 'job_estimate', string='Estimate Lines')
    total_amount = fields.Float('Total', compute='get_total_amount')
    quotation_ref = fields.Many2one('sale.order')

    @api.onchange('customer_id')
    def get_child_ids(self):
        child_ids = []
        if self.customer_id.child_ids:
            for child in self.customer_id.child_ids:
                child_ids.append(child.id)
        return {'domain': {'child_ids': [('id', 'in', child_ids)]}}

    @api.model
    def create(self, vals):
        if vals.get('estimate_name', 'New') == 'New':
            vals['estimate_name'] = self.env['ir.sequence'].next_by_code(
                'job.estimate') or 'New'
        result = super(JobEstimate, self).create(vals)
        return result

    @api.depends('estimate_lines')
    def get_total_amount(self):
        total = 0
        for line in self.estimate_lines:
            total += line.subtotal
        self.total_amount = total

    def button_confirm(self):
        self.state = 'confirmed'

    def create_quotation(self):
        sale_order = self.env['sale.order'].create({
            'state': 'draft',
            'partner_id': self.customer_id.id,
            'payment_details': self.payment_details,
            'estimation_id': self.id,
        })
        for line in self.estimate_lines:
            self.env['sale.order.line'].create({
                'order_id': sale_order.id,
                'product_id': line.product_id.id,
                'product_uom_qty': line.qty,
                'term': line.term,
            })
        self.state = 'quotation'
        self.quotation_ref = sale_order.id


class JobEstimateLine(models.Model):
    _name = 'job.estimate.line'

    product_id = fields.Many2one('product.product', 'Product')
    unit_price = fields.Float('Unit Price')
    qty = fields.Float('Quantity')
    term = fields.Selection([('one_time', 'One Time'), ('monthly', 'Monthly'), ('quarterly', 'Quarterly'), ('yearly', 'Yearly')])
    subtotal = fields.Float('Subtotal', compute='get_subtotal')
    job_estimate = fields.Many2one('job.estimate', 'Job Estimate')

    @api.onchange('product_id')
    def get_product_price(self):
        for rec in self:
            rec.unit_price = rec.product_id.lst_price

    @api.depends('qty', 'unit_price')
    def get_subtotal(self):
        for rec in self:
            rec.subtotal = rec.unit_price * rec.qty