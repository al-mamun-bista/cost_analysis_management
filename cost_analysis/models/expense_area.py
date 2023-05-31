from odoo import models, fields, api, _

class ExpenseArea(models.Model):
    _name = "lc.expense.area"
    _description = "External Expenses"
    _rec_name = 'name'

    name = fields.Char(string="Name",required=True)  
