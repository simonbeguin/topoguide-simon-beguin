from django.shortcuts import get_list_or_404, get_object_or_404, render

from .models import Itineraire


# Create your views here.

def itineraire_list(request):
    """
    Prends les itinéraires créés de données et les affiches
    Get albums from database, either all of them or those matching a POST request
    :param request: The incoming request
    """
    itineraires = get_list_or_404(Itineraire)
    return render(request, 'itineraires/itineraires.html', {'itineraires': itineraires})
