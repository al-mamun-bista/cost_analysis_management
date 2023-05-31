from odoo import models, fields, api, _
from odoo.exceptions import Warning

class BankLoan(models.Model):
    _name = "bank.loan"
    _description = "Bank Loan for Cost Analysis"
    _rec_name = "lc_number"

    loan_amount = fields.Float(_("Loan Amount"))
    advance_amount = fields.Float(_("Advance"))
    due_amount = fields.Float(_("Due Amount"))
    interest = fields.Float(_("Interest"))
    date_issued = fields.Date(_("Date Issued"))
    due_date = fields.Date(_("Due Date"))
    bank_name = fields.Char(string="Bank Name")
    branch_name = fields.Char(string="Branch Name")  
    ac_no = fields.Char(string="A/C No")
    lc_number = fields.Char(string="LC Number")
    lc_id = fields.Many2one("cost.analysis",_("LC"))

    # def open_advance_wizard(self):
    #     if self:
    #         wizard = self.env['bank.loan.wizard'].create({
    #             'loan_amount': self.loan_amount,
    #             'advance_amount':self.advance_amount,
    #             'due_amount':self.due_amount,
    #             'interest':self.interest,
    #             'date_issued':self.date_issued,
    #             'due_date':self.due_date,
    #             'bank_name':self.bank_name,
    #             'branch_name':self.branch_name,
    #             'ac_no':self.ac_no,
    #             'lc_number':self.lc_number,
    #             'lc_id':self.id
    #         })
    #         return {
    #         'name': _('Bank Loan Creation'),
    #         'type': 'ir.actions.act_window',
    #         'res_model': 'bank.loan.wizard',
    #         'view_mode': 'form',
    #         'res_id': wizard.id,
    #         'target': 'new'
    #         }
    #     else:
    #         raise Warning(_("No Self Found"))

class BankLoanWizard(models.TransientModel):
    _name = "bank.loan.wizard"
    _description = "Bank Loan Wizard for Cost Analysis"

    loan_amount = fields.Float(_("Loan Amount"))
    advance_amount = fields.Float(_("Advance"))
    due_amount = fields.Float(_("Due Amount"))
    interest = fields.Float(_("Interest"))
    date_issued = fields.Date(_("Date Issued"))
    due_date = fields.Date(_("Due Date"))
    bank_name = fields.Char(string="Bank Name")
    branch_name = fields.Char(string="Branch Name")  
    ac_no = fields.Char(string="A/C No")
    lc_number = fields.Char(string="LC Number")
    lc_id = fields.Many2one("cost.analysis",_("LC"))

    def create_bank_loan_from_wiz(self):
        if self:
            wizard = self.env['bank.loan'].create({
                'loan_amount': self.loan_amount,
                'advance_amount':self.advance_amount,
                'due_amount':self.loan_amount-self.advance_amount,
                'interest':self.interest,
                'date_issued':self.date_issued,
                'due_date':self.due_date,
                'bank_name':self.bank_name,
                'branch_name':self.branch_name,
                'ac_no':self.ac_no,
                'lc_number':self.lc_number,
                'lc_id':self.lc_id.id
            })
            return {
            'name': _('Bank Loan'),
            'type': 'ir.actions.act_window',
            'res_model': 'bank.loan',
            'view_mode': 'form',
            'res_id': wizard.id,
            'target': 'current'
            }
        else:
            raise Warning(_("No Self Found"))