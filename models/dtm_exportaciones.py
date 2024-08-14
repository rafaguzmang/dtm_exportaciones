from odoo import fields,models,api

class Exportaciones(models.Model):
    _name = "dtm.exportaciones"
    _description = "Modelo para llevar el control de las exportaciones"

    no_cotizacion = fields.Integer(string="No de Cotización", readonly=True)
    proveedor = fields.Selection(selection=[('dtm', 'DISEÑO Y TRANSFORMACIONES METALICAS S DE RL DE CV'), ('mtd', 'METAL TRANSFORMATION & DESIGN')], readonly=True)
    cliente = fields.Char(string="cliente", readonly=True)
    order_compra = fields.Char(string="Orden de Compra", readonly=True)
    fecha_entrada = fields.Date(string="Fecha de Entrada", readonly=True)
    fecha_salida = fields.Date(string="Fecha de Entrega", readonly=True)
    precio_total = fields.Float(string="Precio Total")
    currency = fields.Selection(selection=[('mx','MXN'),('us','USD')], readonly = True)
    packing_list = fields.Binary(string="Packing List")
    odt_ids = fields.Many2many("dtm.compras.items", readonly=True)
    planos_id = fields.Many2many("dtm.exportaciones.planos", readonly=True)
    peso = fields.Char(string="Peso")
    notas = fields.Text()
    foto = fields.Binary(string="Foto")

class Planos(models.Model):
    _name = "dtm.exportaciones.planos"
    _description = "Modelo para guardar los archivos"

    nombre = fields.Char()
    archivo = fields.Binary()
    orden = fields.Char()

