from django.shortcuts import render

from django.views.generic import TemplateView


class PaginaInicialView(TemplateView):
    # Nome do arquivo que vai ser utilizado para renderizar
    # esta página/método/classe
    template_name = "pessoa/index.html"
