from odoo import fields, models, tools

class Award(models.Model):
    _name= "award"
    _description = "Premios"

    description = fields.Char("Descripcion", required=True)
    type = fields.Selection([('Primario','1'),('Secundario','2')], required=True)
    cost = fields.Float("Costo del Premio", required = True)
    status = fields.Boolean("Activo", default=True)

class LotteryModel(models.Model):
    _name="lottery.module"
    _description = "Lista de Rifas"

    event = fields.Char("Evento", required=True)
    quantity_tickets = fields.Integer("Cantidad", required=True)
    start_date = fields.Date("Fecha de Inicio", required =True)
    end_date = fields.Date("Fecha Final", required=True)
    image = fields.Binary("Imagen Publicitaria", required =True)
    award_id = fields.Many2one("award", required=True)
    status = fields.Boolean("Activo", default=True)
    id_customer_winner = fields.Many2one("res_partner", required=True)
    total_sales = fields.Integer("Total Tickets Vendidos")

class Lottery_ticket_line(models.Model):
    _name = "lottery.ticket.line"
    _description = "Boletos de rifa"

    ticket = fields.Integer("Boleto", required=True)
    status = fields.Boolean("Activo", default=True)
    is_winner = fields.Boolean("Ganador", default=False)
    id_lottery = fields.Many2one("lottery.module", required=True)












