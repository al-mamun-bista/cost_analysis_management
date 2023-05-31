from odoo import models, fields, api, _

class ProductList(models.Model):
    _name = "product.list"
    _description = "Product List"
    _rec_name = 'product_id'

    cost_analysis_id = fields.Many2one('cost.analysis',string="Cost Analysis")  
    product_id = fields.Many2one('product.product',string="Product")  
    uom = fields.Many2one('uom.uom',string="UOM")  
    unit_price = fields.Float(string="Unit Price")  
    quantity = fields.Float(string="Quantity")  
    price_global = fields.Float(string="Price Global",compute="_get_calculate_price_global", store=True)

    @api.depends('unit_price','quantity')
    def _get_calculate_price_global(self):
        for ob in self:
            ob.price_global = ob.unit_price * ob.quantity