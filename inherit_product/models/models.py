from odoo import models, fields, api


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    is_percentage_price = fields.Boolean(string='Is Percentage Price')
    percentage_price = fields.Float(string='Percentage Price', default="1")


class PricelistItem(models.Model):
    _inherit = 'product.pricelist.item'

    @api.depends('applied_on', 'compute_price')
    def _compute_price(self):
        for item in self:
            if item.product_tmpl_id.is_percentage_price:
                item.price = item.product_tmpl_id.percentage_price
                item.product_id and item.product_id.product_tmpl_id.sudo().write({'list_price': item.price})
            else:
                super(PricelistItem, item)._compute_price()


class ProductProduct(models.Model):
    _inherit = 'product.product'

    percentage_price = fields.Float(string='Percentage Price', related='product_tmpl_id.percentage_price')


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    percentage_price = fields.Float(string='Percentage Price')
    
    @api.depends('percentage_price')
    def _compute_unit_price(self):
        for line in self:
            if line.percentage_price:
                line.price_unit = 0
            else:
                line.price_unit = line.price_unit
