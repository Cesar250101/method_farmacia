# -*- coding: utf-8 -*-
from odoo import http

# class MethodFarmacia(http.Controller):
#     @http.route('/method_farmacia/method_farmacia/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/method_farmacia/method_farmacia/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('method_farmacia.listing', {
#             'root': '/method_farmacia/method_farmacia',
#             'objects': http.request.env['method_farmacia.method_farmacia'].search([]),
#         })

#     @http.route('/method_farmacia/method_farmacia/objects/<model("method_farmacia.method_farmacia"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('method_farmacia.object', {
#             'object': obj
#         })