from odoo import fields, models, api, _
from datetime import date


class Cheque(models.Model):
    _name = "cheque"

    # CAMPOS DO CHEQUE

    account_cheque = fields.Char()
    cli = fields.Many2one('res.partner', string="Destinatário", default=15)
    num_c = fields.Char(string="Numero do Cheque")
    cod_b = fields.Char(string="Código de Barras")
    ag = fields.Char(string="Agência")
    currency_id = fields.Many2one('res.currency', default=6, Invisible=True)
    valor = fields.Monetary(currency_fields="currency_id", string="Valor")
    destinatario = fields.Many2one('res.partner.bank', string="Banco Destinatario")
    data = fields.Date(string='Data', default=date.today())
    valor_e = fields.Char(string="Valor por Extenço")
    bank_cheque = fields.Many2one(
        "bank_cheque",
        required=True,
        tracking=True
    )
    tipo_c = fields.Selection(
        [
            ('5', 'Comum'),
            ('6', 'Bancário'),
            ('7', 'Salário'),
            ('8', 'Administrativo'),
            ('9', 'CPMF')
        ], string="Tipo de Cheque"
    )

    # CAMPOS ADICIONAIS

    ter = fields.Selection(
        [('sim', 'Sim'),
         ('nao', 'Não')],
        string="Cheque de Terceiros"
    )

    nome = fields.Char(string="Nome")
    cpf = fields.Char(string="CPF")
    tel = fields.Char(string="Telefone")

    @api.onchange("cod_b")
    def on_change_barcode(self):
        for rec in self:
            if rec.cod_b and len(rec.cod_b) == 34:
                rec.bank_cheque = rec.env['bank_cheque'].sudo().search([('cod', 'in', [rec.cod_b[1:4]])])
                rec.ag = rec.cod_b[4:8]
                rec.num_c = rec.cod_b[13:19]
                rec.account_cheque = rec.cod_b[25:32]
            else:
                rec.cod_b = ""

    @api.onchange("valor")
    def on_change_value_code(self):
        currency_id = self.env['res.currency'].browse(self.env.company.currency_id.id)

        for rec in self:
            text_amount = currency_id.amount_to_text(self.valor)
            if text_amount.__eq__("Um Real"):
                rec.valor_e = text_amount
            else:
                rec.valor_e = text_amount.replace("Real", "Reais")

    def Botao(self):
        for rec in self:
            vals_list = {'name': '/',
                         'payment_type': 'outbound',
                         'partner_type': 'customer',
                         'partner_id': rec.cli.id,
                         'destination_account_id': 25,
                         'is_internal_transfer': False,
                         'journal_id': 20,
                         'payment_method_id': 1,
                         'payment_token_id': False,
                         'partner_bank_id': 18,
                         'amount': rec.valor,
                         'currency_id': rec.currency_id.id,
                         'check_amount_in_words': 'Zero Real',
                         'date': rec.data,
                         'effective_date': False,
                         'bank_reference': False,
                         'cheque_reference': False,
                         'ref': False,
                         'edi_document_ids': [],
                         'message_follower_ids': [],
                         'activity_ids': [],
                         'message_ids': []}

            vals_list2 = {'name': '/',
                          'payment_type': 'inbound',
                          'partner_type': 'customer',
                          'partner_id': rec.cli.id,
                          'destination_account_id': 25,
                          'is_internal_transfer': False,
                          'journal_id': 19,
                          'payment_method_id': 1,
                          'payment_token_id': False,
                          'partner_bank_id': 8,
                          'amount': rec.valor,
                          'currency_id': rec.currency_id.id,
                          'check_amount_in_words': 'Zero Real',
                          'date': rec.data,
                          'effective_date': False,
                          'bank_reference': False,
                          'cheque_reference': False,
                          'ref': False,
                          'edi_document_ids': [],
                          'message_follower_ids': [],
                          'activity_ids': [],
                          'message_ids': []}

            pag1 = self.env['account.payment'].create(vals_list)
            pag2 = self.env['account.payment'].create(vals_list2)
            pag1.action_post()
            pag2.action_post()

#
#     return self.env['ir.actions.act_window']._for_xml_id('Banco.banco_wizard_action')
