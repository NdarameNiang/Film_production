from odoo import models, fields, api

class Tournage(models.Model):
    _name = 'cinema.tournage'
    _description = 'Tournage de film'

    numero_tournage = fields.Char(string="Numéro de tournage", required=True)
    date_debut = fields.Date(string="Date de début", required=True)
    date_fin = fields.Date(string="Date de fin", required=True)
    duree_tournage = fields.Integer(string="Durée du tournage", compute='_compute_duree_tournage')
    film_id = fields.Many2one('cinema.film', string="Film tourné", required=True)

    @api.depends('date_debut', 'date_fin')
    def _compute_duree_tournage(self):
        for record in self:
            if record.date_debut and record.date_fin:
                record.duree_tournage = (record.date_fin - record.date_debut).days
            else:
                record.duree_tournage = 0