from odoo import models, fields, api

class MaisonProduction(models.Model):
    _name = 'film.maison_production'
    _description = 'Maison de production'

    name = fields.Char(string='Nom', required=True)
    film_ids = fields.One2many('film.film', 'production_company_id', string='Films produits')
    film_count = fields.Integer(string='Nombre de films', compute='_compute_film_count')
    capital = fields.Float(string='Capital')
	
    @api.depends('film_ids')
    def _compute_film_count(self):
        for record in self:
            record.film_count = len(record.film_ids)
