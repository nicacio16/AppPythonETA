from django.contrib import admin
from .models import Estado, Cidade, Pessoa, Estacao

admin.site.register(Estado)
admin.site.register(Cidade)
admin.site.register(Pessoa)
admin.site.register(Estacao)
