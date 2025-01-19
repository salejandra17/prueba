from odoo import fields, models, tools


class PurchaseLotteryOrder(models.Model):
    _name = "purchase_lottery_order"
    _description = "Ventas de Rifas"

    nro_order = fields.Integer("Numero de Orden", required = True)
    order_date = fields.Date("Fecha de Orden", required=True)
    id_custumer = fields.Many2one("res_partner", required=True)
    quantity_ticket_order = fields.Integer("Cantidad", required=True)
    total_amount = fields.Float("Total Order", required=True)
    status = fields.Char("Estado", required=True)

class PurchaseTicketLine (models.Model):
    _name = "purchase_ticket_line"
    _description = "Compra de Boleto"

    id_lottery = fields.Many2one("lottery.module", required =True)
    id_ticket = fields.Many2one("lottery.ticket.line", required=True)
    id_order = fields.Many2one("purchase.lottery.order", required=True)
    ticket_price = fields.Integer("Precio del boleto", required=True)

class LotteryPayment(models.Model):
    _name = "lottery_payment"
    _description = "Pago de Boleto(s)"

    id_purchase = fields.Many2one("purchase.ticket.line", required =True)
    id_ticket = fields.Many2one("lottery.ticket.line", required=True)
    id_pay_mode = fields.Many2one("payment.mode", required=True)
    pay_amount = fields.Float("Monto a pagar", required=True)
    pay_date =  fields.Date("Fecha de Pago" , required = True)
    id_customer = fields.Many2one("res.partner", required=True)
    confirm = fields.Boolean("Confirmado")


class PaymentMode(models.Model):
    _name = "payment_mode"
    _description = "Forma de Pago"

    id_customer = fields.Many2one("res.partner", required=True)
    payment_mode_name = fields.Char("Banco", required = True)
    ref_number_name = fields.Char("Referencia de pago", required= True)
    bank_name = fields.Char("Banco", required= True)
    owner_bank_name = fields.Char("Titular de la Cuenta", required= True)
    type_id = fields.Integer("Tipo de Identificacion", required = True)
    ci = fields.Integer("Numero de Identificacion", required= True)
