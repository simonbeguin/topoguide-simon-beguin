from unicodedata import name
from django.contrib import admin
from .models import Itineraire


# Register your models here.
class ItineraireAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['titre']}),
        (None,               {'fields': ['point_depart']}),
        (None,               {'fields': ['description']}),
        (None,               {'fields': ['altitude_depart']}),
        (None,               {'fields': ['altitude_minimale']}),
        (None,               {'fields': ['altitude_maximale']}),
        (None,               {'fields': ['denivele_positif_cumule']}),
        (None,               {'fields': ['denivele_negatif_cumule']}),
        (None,               {'fields': ['duree']}),
        (None,               {'fields': ['difficulte']})
    ]
admin.site.register(Itineraire, ItineraireAdmin)
