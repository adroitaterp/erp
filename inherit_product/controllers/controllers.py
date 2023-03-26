# -*- coding: utf-8 -*-
# from odoo import http


# class InheritProduct(http.Controller):
#     @http.route('/inherit_product/inherit_product', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/inherit_product/inherit_product/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('inherit_product.listing', {
#             'root': '/inherit_product/inherit_product',
#             'objects': http.request.env['inherit_product.inherit_product'].search([]),
#         })

#     @http.route('/inherit_product/inherit_product/objects/<model("inherit_product.inherit_product"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('inherit_product.object', {
#             'object': obj
#         })
