from odoo import models, fields, api, _

class CalculateUnitPrice(models.TransientModel):
    _name = "calculate.unit.price"
    _description = "Calculate Unit Price Button Wizard"

    total_price = fields.Float(string="Total Expense")
    # product_list_ids = fields.One2many('product.list.transient','calculate_unit_price_id')
    product_list_ids = fields.Many2many('product.list.transient','calculate_unit_price_rel',default=lambda self: self.env['product.list.transient'].search([]).ids)

class ProductListTransient(models.TransientModel):
    _name = "product.list.transient"
    _description = "ProductListTransient"

    # calculate_unit_price_id = fields.Many2one('calculate.unit.price')  
    product_id = fields.Many2one('product.product',string="Product")  
    uom = fields.Many2one('uom.uom',string="UOM")  
    unit_price = fields.Float(string="Unit Price")  
    quantity = fields.Float(string="Quantity")  
    price_global = fields.Float(string="Price Global") 
    external_expense = fields.Float(string="External Expense") 
    unit_price_total = fields.Float(string="Unit Price Total")  
