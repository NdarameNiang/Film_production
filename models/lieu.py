from odoo import models, fields, api
from datetime import date

class Lieu(models.Model):
    _name = 'tournage.lieu'
    _description = 'Lieu de tournage'
    _rec_name = 'nom'

    nom = fields.Char(string='Nom du lieu', required=True)
    
    # Relation Many2many avec les films
    film_ids = fields.Many2many(
        'tournage.film',
        'tournage_lieu_film_rel',
        'lieu_id',
        'film_id',
        string='Films tournés'
    )
    
    nombre_films = fields.Integer(
        string='Nombre de films tournés',
        compute='_compute_nombre_films',
        store=True
    )

    @api.depends('film_ids')
    def _compute_nombre_films(self):
        for record in self:
            record.nombre_films = len(record.film_ids)

    _sql_constraints = [
        ('nom_unique', 'UNIQUE(nom)', 'Le nom du lieu doit être unique!')
    ]