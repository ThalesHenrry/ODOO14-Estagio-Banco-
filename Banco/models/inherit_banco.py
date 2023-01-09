from odoo import models, fields, api


class banco(models.Model):
    _inherit = "project_request"


    tr = fields.Many2many('account.payment')
    # partner = fields.Many2one(related="payment_id.partner_id")
    # valor = fields.Monetary(related="payment_id.amount")
    # id = fields.Char(related="payment_id.name")
    # data = fields.Date(related="payment_id.date")
    # conta = fields.Many2one(related="payment_id.partner_bank_id")


class pagamento(models.Model):
    _inherit = "account.payment"

    rt = fields.Many2many("project_request")
    # rs = fields.Many2many(related="rt.protocol")
    # ac = fields.Many2many(related="rt.department_views_ids")
