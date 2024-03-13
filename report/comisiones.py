from odoo import api, models, fields, tools

class Comisiones(models.Model):
    _name = 'method_farmacia.comisiones'
    _description = "Comisiones vendedores"
    _auto = False
    _order = 'fecha'

    vendedor_id = fields.Many2one(comodel_name='res.users', strin_idg='Vendedor')
    sku = fields.Char(string='sku')
    nombreproducto = fields.Char(string='nombreproducto')
    pedido = fields.Char(string='pedido')
    fecha = fields.Date(string='fecha')
    cantidad = fields.Integer(string='cantidad')
    price_unit = fields.Integer(string='Precio')
    price_subtotal = fields.Integer(string='Subtotal')
    comision_calculada = fields.Integer(string='comision_calculada')
    tipo_comision = fields.Char(string='Tipo Comisión')
    valor_comision = fields.Float(string='Valor Comisión')

    @api.model_cr
    def init(self):
        user=self.env.uid
        tools.drop_view_if_exists(self._cr, self._table)
        self._cr.execute("""
            CREATE OR REPLACE VIEW %s AS (SELECT 
                    ROW_NUMBER() OVER() AS id,ru.id vendedor_id,pp.default_code sku,pt.name  nombreproducto,po.name pedido,cast(po.date_order as date) fecha,
                    pol.qty cantidad,pol.price_unit,pol.price_subtotal,po.partner_id ,
                    case when pt.tipo_comision ='porc' then  pol.price_subtotal*(pt.valor_comision/100) else valor_comision end comision_calculada,
                    pt.tipo_comision,pt.valor_comision  
                    from pos_order po ,pos_order_line pol ,product_product pp ,product_template pt ,res_users ru 
                    where po.id =pol.order_id 
                    and pol.product_id =pp.id 
                    and pp.product_tmpl_id =pt.id
                    and po.user_id =ru.id
            )
        """ % (
            self._table
            #self._select(), self._from(),user, self._group_by(), self._having(),

        ))