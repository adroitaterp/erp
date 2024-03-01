# -*- coding: utf-8 -*-
# from odoo import http


# class SaleAddations(http.Controller):
#     @http.route('/sale_addations/sale_addations', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sale_addations/sale_addations/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('sale_addations.listing', {
#             'root': '/sale_addations/sale_addations',
#             'objects': http.request.env['sale_addations.sale_addations'].search([]),
#         })

#     @http.route('/sale_addations/sale_addations/objects/<model("sale_addations.sale_addations"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sale_addations.object', {
#             'object': obj
#         })
