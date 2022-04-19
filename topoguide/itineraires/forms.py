from django import forms

from .models import Sortie

class SortieForm(forms.ModelForm):

    class Meta:
        model = Sortie
        fields = '__all__'