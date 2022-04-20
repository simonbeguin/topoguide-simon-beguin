from django import forms

from .models import Sortie

class SortieForm(forms.ModelForm):

    class Meta:
        model = Sortie
        fields = ['itineraire', 'date_sortie', 'duree_reelle', 'nombre_personne', 'experience', 'meteo', 'difficulte_ressentie']