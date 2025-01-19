from odoo import fields, models, tools

class LotteryWinner(models.Model):
    _name = "lettery.winner"
    _description = "Ganador de Loteria"

    id_lottery = fields.Many2one("lottery.module", required =True)
    id_ticket = fields.Many2one("lottery.ticket.line", required=True)
    id_order = fields.Many2one("purchase.lottery.order", required=True)
    id_award = fields.Many2one("award", required=True)
    id_customer_winner = fields.Many2one("res_partner", required=True)
    id_lottery_payment = fields.Many2one("lottery.payment", required=True)

