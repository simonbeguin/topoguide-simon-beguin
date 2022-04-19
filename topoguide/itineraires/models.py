from django.db import models
from django.contrib import admin
from django.db.models import IntegerField, Model

# Create your models here.

class Itineraire(models.Model):
    """
    Un itinéraire constitué du titre, du point de départ, de la description, de l'altitude de départ, 
    de l'altitude min, de l'altitude max, du dénivelé positif cumulé
    du dénivelé négatif cumulé dela durée estimée (en heures) de la difficulté estimée (de 1 à 5)
    """
    titre = models.CharField(max_length=200)
    point_depart = models.CharField(max_length=200)
    description = models.CharField(max_length=400)
    altitude_depart = models.FloatField()
    altitude_minimale = models.FloatField()
    altitude_maximale = models.CharField(max_length=200)
    denivele_positif_cumule = models.FloatField()
    denivele_negatif_cumule = models.FloatField()
    duree = models.FloatField()
    CHOIX_DIF = ((1,'1'),(2,'2'),(3,'3'), (4,'4'), (5,'5'))
    difficulte = models.IntegerField(default=1,choices=CHOIX_DIF)

    

    
    def __str__(self):
        return self.titre
    
    