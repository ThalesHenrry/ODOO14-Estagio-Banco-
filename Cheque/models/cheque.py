from odoo import fields, models, api, _
from datetime import date


class Cheque(models.Model):
    _name = "cheque"

    num_c = fields.Char(string="Numero do Cheque")
    cod_b = fields.Char(string="Código de Barras")
    ag = fields.Char(string="Agência")
    destinatario = fields.Many2one('res.partner.bank', string="Banco Destinatario")
    dest = fields.Many2one('account.account', string="Conta Transitórioa", Default=555)
    currency_id = fields.Many2one('res.currency', default=6, Invisible=True)
    valor = fields.Monetary(currency_fields="currency_id", string="Valor")
    data = fields.Date(string='Data', default=date.today())
    valor_e = fields.Char(string="Valor por Extençaõ")
    bank_id = fields.Many2one('res.bank')
    tipo_c = fields.Selection(
        [
            ('5', 'Comum'),
            ('6', 'Bancário'),
            ('7', 'Salário'),
            ('8', 'Administrativo'),
            ('9', 'CPMF')
        ], string="Tipo de Cheque"
    )
