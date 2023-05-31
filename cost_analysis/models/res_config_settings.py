from odoo import models, fields, api, _
from odoo.exceptions import Warning

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    cost_journal = fields.Many2one(comodel_name="account.journal",string="Expense Journal", config_parameter="cost_analysis.cost_journal")
    cost_account = fields.Many2one(comodel_name="account.account",string="Expense Account", config_parameter="cost_analysis.cost_account")
    