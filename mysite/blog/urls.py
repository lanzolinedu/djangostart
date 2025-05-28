from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('indice', views.indice, name='indice'),
    path('musica', views.musica, name='musica'),
    path('film', views.film, name='film'),
]