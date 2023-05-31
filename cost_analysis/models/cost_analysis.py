from odoo import models, fields, api, _
from odoo.exceptions import Warning

class CostAnalysis(models.Model):
    _name = "cost.analysis"
    _description = "Cost Analysis"
    _rec_name = 'lc_number'


    lc_number = fields.Char(string="LC Number")  
    initial_date = fields.Date(string="Initial Date")  
    validation_date = fields.Date(string="Validation Date")  
    partner_id = fields.Many2one('res.partner',string="Partner")  
    bank_name = fields.Char(string="Bank Name")
    branch_name = fields.Char(string="Branch Name")  
    ac_no = fields.Char(string="A/C No")  
    currency = fields.Char(string="Currency")  
    conversion_rate = fields.Float(string="Conversion Rate")  
    product_list_ids = fields.One2many('product.list','cost_analysis_id')
    expense_area_ids = fields.One2many('external.expenses','cost_analysis_id')
    total_price  = fields.Float(string="Total Cost",compute="_get_calculate_total_price", store=True)
    total_expense  = fields.Float(string="Total Expense",compute="_get_calculate_total_expense", store=True)

    @api.depends('product_list_ids')
    def _get_calculate_total_price(self):
        _total_price = 0
        for ob in self.product_list_ids:
            _total_price += ob.price_global
        self.total_price = _total_price

    @api.depends('expense_area_ids')
    def _get_calculate_total_expense(self):
        _total_expense = 0
        for ob in self.expense_area_ids:
            _total_expense += ob.amount
        self.total_expense = _total_expense

    def post_all_expenses_button(self):
        pass

    def create_po_button(self):
        pass

    def calculate_unit_price_button(self):
        if self.conversion_rate == 0:
            raise Warning('Please set the conversion rate.')
        form_view_id = self.env.ref('cost_analysis.view_calculate_unit_price_form')
        product_list_transient_model = self.env['product.list.transient']
        for ob in product_list_transient_model.search([]):
            ob.unlink()
        for line in self.product_list_ids:
            external_expense = self.total_expense*(line.price_global*100/self.total_price)/100
            unit_price_total = line.price_global+external_expense/line.quantity
            product_line = {
                    'product_id': line.product_id.id,
                    'uom' : line.uom.id,
                    'unit_price' : line.unit_price*self.conversion_rate,
                    'quantity' : line.quantity,
                    'price_global' : line.price_global*self.conversion_rate,
                    'external_expense' : external_expense*self.conversion_rate,
                    'unit_price_total' : unit_price_total*self.conversion_rate,
                }
            product_list_transient_model.create(product_line)
        
        return {
            'type': 'ir.actions.act_window',
            'name': _('Calculate Unit Price'),
            'res_model': 'calculate.unit.price',
            'view_mode': 'form',
            'view_id': form_view_id.id,
            'target': 'new',
        }

    def open_advance_wizard(self):
        if self:
            wizard = self.env['bank.loan.wizard'].create({
                'loan_amount': self.total_price,
                'advance_amount':"",
                'due_amount':"",
                'interest':"",
                'date_issued':None,
                'due_date':None,
                'bank_name':self.bank_name,
                'branch_name':self.branch_name,
                'ac_no':self.ac_no,
                'lc_number':self.lc_number,
                'lc_id':self.id
            })
            return {
            'name': _('Bank Loan Creation'),
            'type': 'ir.actions.act_window',
            'res_model': 'bank.loan.wizard',
            'view_mode': 'form',
            'res_id': wizard.id,
            'target': 'new'
            }
        else:
            raise Warning(_("No Self Found"))
