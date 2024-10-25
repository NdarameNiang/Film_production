from odoo import models, fields, api

class MaisonProduction(models.Model):
    _name = 'maison.production'
    _description = 'Maison de Production'

    name = fields.Char('Nom', required=True)
    film_ids = fields.One2many('film', 'production_company_id', string='Films')
    film_count = fields.Integer(string='Nombre de films', compute='_compute_film_count')
    capital = fields.Float('Capital')

    @api.depends('film_ids')
    def _compute_film_count(self):
        for maison in self:
            maison.film_count = len(maison.film_ids)

