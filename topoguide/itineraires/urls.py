from django.urls import path

from . import views

app_name = 'itineraires'
urlpatterns = [
    path('', views.itineraire_list, name='itineraire_list'),
    path('sorties/<int:itineraire_id>/', views.sortie_list, name='sortie_list')
]