from django.shortcuts import get_list_or_404, get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .forms import SortieForm
from .models import Itineraire, Sortie


# Create your views here.

@login_required
def itineraires(request):
    """
    Prends les itinéraires créés et les affiches
    """
    itineraires = get_list_or_404(Itineraire)
    return render(request, 'itineraires/itineraires.html', {'itineraires': itineraires})


@login_required
def sorties(request, itineraire_id):
    """
    Prends les sorties créés  et les affiches
    """
    sorties  = get_list_or_404(Sortie, itineraire_id = itineraire_id)
    itineraire = get_object_or_404(Itineraire, pk = itineraire_id)
    utilisateur = request.user
    return render(request, 'itineraires/sorties.html', {'sorties': sorties, 'itineraire': itineraire, 'utilisateur':utilisateur})

@login_required
def sortie(request, sortie_id):
    """
    Prend une sortie et affiche les détails
    """
    sortie = get_object_or_404(Sortie, pk=sortie_id)
    return render(request, 'itineraires/sorties_details.html', {'sortie': sortie})

@login_required
def nouvelle_sortie(request):
    """
    Crée une nouvelle sortie
    """
    if request.method == "POST":
        form = SortieForm(request.POST)
        if form.is_valid():
            sortie = form.save(commit=False)
            sortie.author = request.user
            sortie.published_date = timezone.now()
            sortie.save()
            return redirect('itineraires:sortie_details', pk = sortie.pk)
    else:
        form = SortieForm()
    return render(request, 'itineraires/modif_sortie.html', {'form': form})

@login_required
def modif_sortie(request, sortie_id):
    sortie = get_object_or_404(Sortie, pk=sortie_id)
    if request.method == "POST":
        form = SortieForm(request.POST, instance=sortie)
        if form.is_valid():
            sortie = form.save(commit=False)
            sortie.author = request.user
            sortie.published_date = timezone.now()
            sortie.save()
            return redirect('itineraires:sortie_details', sortie_id)
    else:
        form = SortieForm(instance=sortie)
    return render(request, 'itineraires/modif_sortie.html', {'form': form})



