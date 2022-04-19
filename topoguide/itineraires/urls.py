from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .import views

app_name = 'itineraires'
urlpatterns = [
    path('', views.itineraires, name='itineraires'),
    path('sorties/<int:itineraire_id>/', views.sorties, name='sorties'),
    path('sortie/<int:sortie_id>/', views.sortie, name='sortie_details'),
    path('nouvelle_sortie/', views.nouvelle_sortie, name='nouvelle_sortie')
    ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)