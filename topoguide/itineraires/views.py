from django.shortcuts import get_list_or_404, get_object_or_404, render
from django.contrib.auth.decorators import login_required

from .models import Itineraire, Sortie


# Create your views here.

@login_required()
def itineraires(request):
    """
    Prends les itinéraires créés de données et les affiches
    """
    itineraires = get_list_or_404(Itineraire)
    return render(request, 'itineraires/itineraires.html', {'itineraires': itineraires})


@login_required()
def sorties(request, itineraire_id):
    """
    Prends les sorties créés de données et les affiches
    """
    sorties  = get_list_or_404(Sortie, pk = itineraire_id)
    return render(request, 'itineraires/sorties.html', {'sorties': sorties})

