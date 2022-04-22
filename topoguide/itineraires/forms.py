from django import forms

from .models import Sortie

class SortieForm(forms.ModelForm):
    """
    Simple formulaire, choix des items à afficher
    """
    class Meta:
        model = Sortie
        fields = ['date_sortie', 'duree_reelle', 'nombre_personne', 'experience', 'meteo', 'difficulte_ressentie']