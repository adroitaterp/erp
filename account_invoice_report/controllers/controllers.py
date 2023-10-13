# -*- coding: utf-8 -*-
# from odoo import http


# class /mnt/extra-addons/accountInvoiceReport(http.Controller):
#     @http.route('//mnt/extra-addons/account_invoice_report//mnt/extra-addons/account_invoice_report/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('//mnt/extra-addons/account_invoice_report//mnt/extra-addons/account_invoice_report/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('/mnt/extra-addons/account_invoice_report.listing', {
#             'root': '//mnt/extra-addons/account_invoice_report//mnt/extra-addons/account_invoice_report',
#             'objects': http.request.env['/mnt/extra-addons/account_invoice_report./mnt/extra-addons/account_invoice_report'].search([]),
#         })

#     @http.route('//mnt/extra-addons/account_invoice_report//mnt/extra-addons/account_invoice_report/objects/<model("/mnt/extra-addons/account_invoice_report./mnt/extra-addons/account_invoice_report"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('/mnt/extra-addons/account_invoice_report.object', {
#             'object': obj
#         })
