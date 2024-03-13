# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    tipo_comision = fields.Selection([
        ('pesos', '$'),
        ('porc', '%')
    ], string='Tipo Comisión')
    
    valor_comision = fields.Float(string='Valor Comisión')