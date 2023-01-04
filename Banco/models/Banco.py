from odoo import fields, models, api, _
from datetime import date


class Banco(models.Model):
    _name = "banco"

    co = fields.Integer(string='Conta Origem')
    cd = fields.Integer(string='Conta Destino')
    data = fields.Date(string='Data', default=date.today())

    cli = fields.Many2one('res.partner', string="Destinatário")
    remetente = fields.Many2one('res.partner.bank', string="Banco Remetente")
    destinatario = fields.Many2one('res.partner.bank', string="Banco Destinatario")
    currency_id = fields.Many2one('res.currency', default=6)
    dest = fields.Many2one('account.account', string="Conta partida")
    currency_valor = fields.Monetary(currency_field="currency_id", string="Montante")
    diario = fields.Many2one('account.journal', string="Diário")

    def butao(self):
        vals_list = {'name': '/',
                     'payment_type': 'outbound',
                     'partner_type': 'customer',
                     'partner_id': self.cli.id,
                     'destination_account_id': 25,
                     'is_internal_transfer': False,
                     'journal_id': self.diario.id,
                     'payment_method_id': 1,
                     'payment_token_id': False,
                     'partner_bank_id': self.remetente.id,
                     'amount': self.currency_valor,
                     'currency_id': self.currency_id.id,
                     'check_amount_in_words': 'Zero Real',
                     'date': self.data,
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
                      'partner_id': self.cli.id,
                      'destination_account_id': 25,
                      'is_internal_transfer': False,
                      'journal_id': self.diario.id,
                      'payment_method_id': 1,
                      'payment_token_id': False,
                      'partner_bank_id': self.destinatario.id,
                      'amount': self.currency_valor,
                      'currency_id': self.currency_id.id,
                      'check_amount_in_words': 'Zero Real',
                      'date': self.data,
                      'effective_date': False,
                      'bank_reference': False,
                      'cheque_reference': False,
                      'ref': False,
                      'edi_document_ids': [],
                      'message_follower_ids': [],
                      'activity_ids': [],
                      'message_ids': []}

        self.env['account.payment'].create(vals_list)
        self.env['account.payment'].create(vals_list2)

        return self.env['ir.actions.act_window']._for_xml_id('Banco.banco_wizard_action')


