from odoo import models, fields

class Film(models.Model):
    _name = 'cinema.film'
    _description = 'Film'

    name = fields.Char(string="Nom", required=True)
    tournage_ids = fields.One2many('cinema.tournage', 'film_id', string="Tournages")
