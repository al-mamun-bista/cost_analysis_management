from odoo import models, fields, api, _

class ExternalExpenses(models.Model):
    _name = "external.expenses"
    _description = "External Expenses"
    _rec_name = 'expense_area_id'

    cost_analysis_id = fields.Many2one('cost.analysis',string="Cost Analysis")  
    expense_area_id = fields.Many2one('lc.expense.area',string="Expense Area")  
    details = fields.Char(string="Details")  
    amount = fields.Float(string="Amount")
    status = fields.Selection([('posted', 'Posted'), ('draft', 'Draft')],string="Status")

    def post_button(self):
        pass