from odoo import fields, models, api, _
from datetime import date


class Cheque(models.Model):
    _name = "lote"

    campo_cheque = fields.Many2many('cheque')
