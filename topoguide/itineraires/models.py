from django.db import models
from django.contrib import admin
from django.db.models import IntegerField, Model
from django.contrib.auth.decorators import login_required

# Create your models here.

#@login_required
class Itineraire(models.Model):
    """
    Un itinéraire constitué du titre, du point de départ, de la description, de l'altitude de départ, 
    de l'altitude min, de l'altitude max, du dénivelé positif cumulé
    du dénivelé négatif cumulé dela durée estimée (en heures) de la difficulté estimée (de 1 à 5)
    """
    titre = models.CharField(max_length=200)
    point_depart = models.CharField('Point de départ',max_length=200)
    description = models.CharField(max_length=400)
    altitude_depart = models.FloatField('Altitude de départ (m)')
    altitude_minimale = models.FloatField('Altitude minimale (m)')
    altitude_maximale = models.FloatField('Altitude maximale (m)')
    denivele_positif_cumule = models.FloatField('Dénivelé positif cumulé (m)')
    denivele_negatif_cumule = models.FloatField('Dénivelé négatif cumulé (m)')
    duree = models.FloatField('Durée (en heure)')
    CHOIX_DIF = ((1,'1'),(2,'2'),(3,'3'), (4,'4'), (5,'5'))
    difficulte = models.IntegerField('Difficulté (de 1 à 5)', default=1,choices=CHOIX_DIF)

    

    
    def __str__(self):
        return self.titre
    
    