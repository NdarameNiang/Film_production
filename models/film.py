from odoo import models, fields, api
class Film(models.Model):
    _name = 'film'
    _description = 'Film'

    name = fields.Char('Nom', required=True)
    release_date = fields.Date('Date de sortie')
    duration = fields.Float('Durée')
    director_id = fields.Many2one('realisateur', string='Réalisateur')
    location_id = fields.Many2one('lieu', string='Lieu Tourné')
    production_company_id = fields.Many2one('maison.production', string='Maison de Production')
    film_type = fields.Selection([('fiction', 'Fiction'), ('documentaire', 'Documentaire')], string='Type de film')
    size = fields.Float('Taille du Film (GB)')
    price_sold = fields.Float('Prix vendu')
