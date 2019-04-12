# módulo do Django para criar urls
from django.urls import path

# Importe todas suas classes do views.py
from .views import *

urlpatterns = [
# path('caminho/da/url', ClasseLáDoView.as_view(), name="nomeDessaURL" )
path('', PaginaInicialView.as_view(), name="index"),
path('contato/', ContatoView.as_view(), name="contato"),
path('sobre/', SobreView.as_view(), name="sobre"),
path('team/', TeamView.as_view(), name="team"),
path('curriculo/', CurriculoView.as_view(), name="curriculo"),

]
