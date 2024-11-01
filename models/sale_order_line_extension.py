from odoo import models, fields, api

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    @api.model
    def create(self, vals):
        # Llama al super para crear la línea de venta
        record = super(SaleOrderLine, self).create(vals)
        
        # Verifica si el producto es "Tiempo Aire" y ejecuta la acción si es así
        product = self.env['product.product'].browse(vals.get('product_id'))
        if product and product.name == "Tiempo Aire":
            self._execute_custom_action(record)

        return record

    def _execute_custom_action(self, sale_line):
        # Aquí puedes agregar cualquier lógica en Python que desees ejecutar
        # cuando se venda el producto "Tiempo Aire".
        print("Acción ejecutada: Se ha vendido el producto Tiempo Aire")
        # Aquí puedes agregar cualquier otra lógica que necesites

