from odoo import models, fields, api

class Film(models.Model):
    _name = 'tournage.film'
    _description = 'Film'
    _rec_name = 'nom'
    _sql_constraints = [
        ('nom_unique', 'UNIQUE(nom)', 'Le nom du film doit être unique!')
    ]

    # Champs de base
    nom = fields.Char(
        string='Nom du film',
        required=True,
    )
    
    date_sortie = fields.Date(
        string='Date de sortie',
        required=True,
    )
    
    duree = fields.Float(
        string='Durée (heures)',
        digits=(4, 2),  # 4 chiffres au total, 2 après la virgule
        required=True,
    )
    
    type_film = fields.Selection([
        ('action', 'Action'),
        ('comedie', 'Comédie'),
        ('drame', 'Drame'),
        ('sci_fi', 'Science Fiction'),
        ('documentaire', 'Documentaire'),
        ('animation', 'Animation'),
        ('thriller', 'Thriller'),
        ('horreur', 'Horreur')
    ], string='Type de film', required=True)
    
    taille = fields.Float(
        string='Taille (Go)',
        digits=(10, 2),
    )
    
    prix_vendu = fields.Float(
        string='Prix de vente (€)',
        digits=(10, 2),
    )

    # Relations avec d'autres modèles
    realisateur_id = fields.Many2one(
        'tournage.realisateur',
        string='Réalisateur',
        required=True,
        ondelete='restrict'
    )

    lieu_ids = fields.Many2many(
        'tournage.lieu',
        string='Lieux de tournage',
        required=True
    )

  

  
    # Champs calculés
    duree_minutes = fields.Integer(
        string='Durée (minutes)',
        compute='_compute_duree_minutes',
        store=True
    )

 

    # Méthodes calculées
    @api.depends('duree')
    def _compute_duree_minutes(self):
        for record in self:
            record.duree_minutes = int(record.duree * 60)

    # Contraintes
    @api.constrains('duree')
    def _check_duree(self):
        for record in self:
            if record.duree <= 0:
                raise models.ValidationError('La durée du film doit être supérieure à 0!')

    @api.constrains('prix_vendu')
    def _check_prix(self):
        for record in self:
            if record.prix_vendu and record.prix_vendu < 0:
                raise models.ValidationError('Le prix de vente ne peut pas être négatif!')

    @api.constrains('taille')
    def _check_taille(self):
        for record in self:
            if record.taille and record.taille < 0:
                raise models.ValidationError('La taille du film ne peut pas être négative!')

    # # Méthodes ORM surchargées
    # @api.model
    # def create(self, vals):
    #     # Code à exécuter avant la création
    #     return super(Film, self).create(vals)

    # def write(self, vals):
    #     # Code à exécuter avant la modification
    #     return super(Film, self).write(vals)

    # def unlink(self):
    #     # Vérifications avant la suppression
    #     for record in self:
    #         if record.statut == 'en_tournage':
    #             raise models.ValidationError('Impossible de supprimer un film en cours de tournage!')
    #     return super(Film, self).unlink()

    # # Méthodes d'action
    # def action_start_tournage(self):
    #     for record in self:
    #         record.statut = 'en_tournage'

    # def action_finish_tournage(self):
    #     for record in self:
    #         record.statut = 'post_production'

    # def action_cancel_film(self):
    #     for record in self:
    #         record.statut = 'annule'

    # def action_complete_film(self):
    #     for record in self:
    #         record.statut = 'termine'