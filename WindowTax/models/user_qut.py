from odoo import models, fields,api

class UserQut(models.Model):
    _name = 'user.qut'
    _description = 'User Qut Description'

    # Define fields here
    name = fields.Char(string='To')
    partner_id = fields.Many2one('res.partner', string='To')
    num = fields.Char(string='Number')
    email = fields.Char(string='Email')
    attn = fields.Char(string='Attn')
    Date = fields.Datetime('Date', default=lambda self: fields.Datetime.now())
    pyment = fields.Char(string='Pyment Terms')
    total = fields.Float(string='Total', compute='_compute_total', store=True)
    paid = fields.Float(string='paid')
    qut_line_ids = fields.One2many('qut.line', 'qut_id', string='Lines')
    question = fields.Boolean(string ='Question')
    @api.depends('qut_line_ids.total_price')
    def _compute_total(self):
        for record in self:
            record.total = sum(line.total_price for line in record.qut_line_ids)
    @api.onchange('qut_line_ids')
    def _onchange_qut_line_ids(self):
        self._compute_total()  # Recalculate total on change)

    @api.onchange('partner_id')
    def _onchange_qut_line_ids(self):
        self.num=self.partner_id.phone
        self.email=self.partner_id.email


class QutLine(models.Model):
    _name = 'qut.line'
    description = fields.Char(string='Description')
    line_total = fields.Float(string='Line Total')
    qty = fields.Float(string='Qty')
    total_price = fields.Float(string='Total Pprice')
    qut_id = fields.Many2one('user.qut')
