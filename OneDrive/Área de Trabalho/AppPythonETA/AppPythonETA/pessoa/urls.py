# módulo do Django para criar urls
from django.urls import path

# Importe todas suas classes do views.py
from .views import *

urlpatterns = [
# path('caminho/da/url', ClasseLáDoView.as_view(), name="nomeDessaURL" )
path('', PaginaInicialView.as_view(), name="index"),
path('sobre/', SobreView.as_view(), name="sobre"),
path('contato/', ContatoView.as_view(), name="contato"),
path('curriculo/', CurriculoView.as_view(), name="curriculo"),
path('team/', TeamView.as_view(), name="team"),
path('cadastroETA/', CadastroETAView.as_view(), name="cadastroETA"),

# URLS de Estado
path('cadastrar/estado/', EstadoCreate.as_view(), name="cadastrar-estado"),
path('editar/estado/<int:pk>/', EstadoUpdate.as_view(), name="editar-estado"),
path('excluir/estado/<int:pk>/', EstadoDelete.as_view(), name="excluir-estado"),
path('listar/estado/', EstadoList.as_view(), name="listar-estados"),

# URLS de Cidade
path('cadastrar/cidade/', CidadeCreate.as_view(), name="cadastrar-cidade"),
path('editar/cidade/<int:pk>/', CidadeUpdate.as_view(), name="editar-cidade"),
path('excluir/cidade/<int:pk>/', CidadeDelete.as_view(), name="excluir-cidade"),
path('listar/cidade/', CidadeList.as_view(), name="listar-cidades"),

# URLS de Pessoa
# path('cadastrar/pessoa/', PessoaCreate.as_view(), name="cadastrar-pessoa"),
path('editar/pessoa/<int:pk>/', PessoaUpdate.as_view(), name="editar-pessoa"),
# path('excluir/pessoa/<int:pk>/', PessoaDelete.as_view(), name="excluir-pessoa"),
path('listar/pessoa/', PessoaList.as_view(), name="listar-pessoas"),

# URLS de Tipo de Estação
path('cadastrar/tipo-estacao/', TipoEstacaoCreate.as_view(), name="cadastrar-tipo-estacao"),
path('editar/tipo-estacao/<int:pk>/', TipoEstacaoUpdate.as_view(), name="editar-tipo-estacao"),
path('excluir/tipo-estacao/<int:pk>/', TipoEstacaoDelete.as_view(), name="excluir-tipo-estacao"),
path('listar/tipo-estacao/', TipoEstacaoList.as_view(), name="listar-tipo-estacao"),

# URLS de Estacao
path('cadastrar/estacao/', EstacaoCreate.as_view(), name="cadastrar-estacao"),
path('editar/estacao/<int:pk>/', EstacaoUpdate.as_view(), name="editar-estacao"),
path('excluir/estacao/<int:pk>/', EstacaoDelete.as_view(), name="excluir-estacao"),
path('listar/estacao/', EstacaoList.as_view(), name="listar-estacao"),

# URLS de Sensor
path('cadastrar/sensor/', SensorCreate.as_view(), name="cadastrar-sensor"),
path('editar/sensor/<int:pk>/', SensorUpdate.as_view(), name="editar-sensor"),
path('excluir/sensor/<int:pk>/', SensorDelete.as_view(), name="excluir-sensor"),
path('listar/sensor/', SensorList.as_view(), name="listar-sensor"),

# URLS de Historico de Consumo
path('cadastrar/historico-consumo/', HistoricoConsumoCreate.as_view(), name="cadastrar-historico-consumo"),
path('editar/historico-consumo/<int:pk>/', HistoricoConsumoUpdate.as_view(), name="editar-historico-consumo"),
path('excluir/historico-consumo/<int:pk>/', HistoricoConsumoDelete.as_view(), name="excluir-historico-consumo"),
path('listar/historico-consumo/', HistoricoConsumoList.as_view(), name="listar-historico-consumo"),




]
