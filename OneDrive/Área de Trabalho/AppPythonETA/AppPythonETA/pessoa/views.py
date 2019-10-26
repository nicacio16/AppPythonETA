from django.shortcuts import render

# Importa o Mixin para obrigar login
from django.contrib.auth.mixins import LoginRequiredMixin

from braces.views import GroupRequiredMixin

# Importa todas as classes do models.py
from .models import *

# Importa função que vai chamar as urls pelo "name" delas
from django.urls import reverse_lazy

# Importar as classes Views para inserir, alterar e excluir utilizando formulários
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Importa o TemplateView para criação de páginas simples
from django.views.generic import TemplateView

# Importa ListView para gerar as telas com tabelas
from django.views.generic.list import ListView

# Método que busca um objeto. Se não existir, da um erro 404
from django.shortcuts import get_object_or_404





# Create your views here.

# Cria uma classe com herança de TemplateView para exibir
# um arquivo HTML normal (com o conteúdo dele)


class PaginaInicialView(TemplateView):
    # Nome do arquivo que vai ser utilizado para renderizar
    # esta página/método/classe
    template_name = "index.html"

    # Método utilizado para enviar dados ao template
    def get_context_data(self, *args, **kwargs):
            # Chamar o "pai" para que sempre tenha o comportamento padrão, além do nosso
            context = super(PaginaInicialView, self).get_context_data(
                *args, **kwargs)
            context['ultimos_lancamentos'] = Estacao.objects.all().reverse()[0:10]
            return context

# Página "Sobre"


class SobreView(TemplateView):
    template_name = "sobre.html"

# Pagina de "Contato"


class ContatoView(TemplateView):
    template_name = "contato.html"

# Página "Curriculo"


class CurriculoView(TemplateView):
    template_name = "curriculo.html"

# Pagina de "Team"


class TeamView(TemplateView):
    template_name = "team.html"

# Página "CadastroETA"


class CadastroETAView(TemplateView):
    template_name = "cadastroETA.html"

##################### CRIAR ######################


class EstadoCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    group_required = u"Administrador"
    # Define qual o modelo pra essa classe vai criar o form
    model = Estado
    # Qual o html que será utilizado?
    template_name = "formulario.html"
    # Pra onde redirecionar o usuário depois de inserir um registro. Informe o nome da url
    success_url = reverse_lazy("listar-estados")
    # Quais campos devem aparecer no formulário?
    fields = ['sigla', 'nome']

    # Método utilizado para enviar dados ao template
    def get_context_data(self, *args, **kwargs):
        # Chamar o "pai" para que sempre tenha o comportamento padrão, além do nosso
        context = super(EstadoCreate, self).get_context_data(*args, **kwargs)

        # Adicionar coisas ao contexto que serão enviadas para o html
        context['titulo'] = "Cadastro de novos Estados"
        context['botao'] = "Cadastrar"
        context['classeBotao'] = "btn-primary"

        # Devolve/envia o context para seu comportamento padrão
        return context


class CidadeCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    group_required = u"Administrador"
    model = Cidade
    template_name = "formulario.html"
    success_url = reverse_lazy("listar-cidades")
    fields = ['nome', 'estado']

    # Método utilizado para enviar dados ao template
    def get_context_data(self, *args, **kwargs):
        context = super(CidadeCreate, self).get_context_data(*args, **kwargs)
        context['titulo'] = "Cadastro de novas Cidades"
        context['botao'] = "Cadastrar"
        context['classeBotao'] = "btn-primary"
        return context
    

class PessoaCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    group_required = u"Usuário"
    model = Pessoa
    template_name = "formulario.html"
    success_url = reverse_lazy("listar-pessoas")
    fields = ['nome', 'nascimento', 'email', 'cidade']

    # Método utilizado para enviar dados ao template
    def get_context_data(self, *args, **kwargs):
        context = super(PessoaCreate, self).get_context_data(*args, **kwargs)
        context['titulo'] = "Cadastro de novos Usuários"
        context['botao'] = "Cadastrar"
        context['classeBotao'] = "btn-primary"
        return context


class TipoEstacaoCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    group_required = u"Administrador"
    model = Estacao
    template_name = "formulario.html"
    success_url = reverse_lazy("listar-tipo-estacao")
    fields = ['tipo']

    def form_valid(self, form):

        # Define o usuário como usuário logado
        form.instance.usuario = self.request.user

        url = super().form_valid(form)

        return url

    # Método utilizado para enviar dados ao template
    def get_context_data(self, *args, **kwargs):
        context = super(TipoEstacaoCreate, self).get_context_data(*args, **kwargs)
        context['titulo'] = "Cadastro de novos tipos de Estação"
        context['botao'] = "Cadastrar"
        context['classeBotao'] = "btn-primary"
        return context


class EstacaoCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    group_required = u"Usuário"
    model = Estacao
    template_name = "formulario.html"
    success_url = reverse_lazy("listar-estacao")
    fields = ['local', 'capacidade', 'cidade']
    
    def form_valid(self, form):

        # Define o usuário como usuário logado
        form.instance.usuario = self.request.user

        url = super().form_valid(form)

        return url

    # Método utilizado para enviar dados ao template
    def get_context_data(self, *args, **kwargs):
        context = super(EstacaoCreate, self).get_context_data(*args, **kwargs)
        context['titulo'] = "Cadastro de novas Etas"
        context['botao'] = "Cadastrar"
        context['classeBotao'] = "btn-primary"
        return context


class SensorCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    group_required = u"Usuário"
    model = Sensor
    template_name = "formulario.html"
    success_url = reverse_lazy("listar-sensor")
    fields = ['idsensor', 'tipo', 'estacao']

    def form_valid(self, form):

        # Define o usuário como usuário logado
        form.instance.usuario = self.request.user

        url = super().form_valid(form)

        return url

    # Método utilizado para enviar dados ao template
    def get_context_data(self, *args, **kwargs):
        context = super(SensorCreate, self).get_context_data(*args, **kwargs)
        context['titulo'] = "Cadastro de Sensor"
        context['botao'] = "Cadastrar"
        context['classeBotao'] = "btn-primary"
        return context


class HistoricoConsumoCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    group_required = u"Usuário"
    model = HistoricoConsumo
    template_name = "formulario.html"
    success_url = reverse_lazy("listar-historico-consumo")
    fields = ['mes', 'ano', 'quantidade', 'valor']

    def form_valid(self, form):

        # Define o usuário como usuário logado
        form.instance.usuario = self.request.user

        url = super().form_valid(form)

        return url

    # Método utilizado para enviar dados ao template
    def get_context_data(self, *args, **kwargs):
        context = super(HistoricoConsumoCreate, self).get_context_data(*args, **kwargs)
        context['titulo'] = "Cadastro de Historico de Consumo"
        context['botao'] = "Cadastrar"
        context['classeBotao'] = "btn-primary"
        return context


##################### EDITAR ######################


class EstadoUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    group_required = u"Administrador"
    # Define qual o modelo pra essa classe vai criar o form
    model = Estado
    # Qual o html que será utilizado?
    template_name = "formulario.html"
    # Pra onde redirecionar o usuário depois de editar um registro. Informe o nome da url
    success_url = reverse_lazy("listar-estados")
    # Quais campos devem aparecer no formulário?
    fields = ['sigla', 'nome']

    # Método utilizado para enviar dados ao template
    def get_context_data(self, *args, **kwargs):
        # Chamar o "pai" para que sempre tenha o comportamento padrão, além do nosso
        context = super(EstadoUpdate, self).get_context_data(*args, **kwargs)

        # Adicionar coisas ao contexto que serão enviadas para o html
        context['titulo'] = "Editar cadastro de Estado"
        context['botao'] = "Salvar"
        context['classeBotao'] = "btn-success"

        # Devolve/envia o context para seu comportamento padrão
        return context


class CidadeUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    group_required = u"Administrador"
    model = Cidade
    template_name = "formulario.html"
    success_url = reverse_lazy("listar-cidades")
    fields = ['nome', 'estado']

    # Método utilizado para enviar dados ao template
    def get_context_data(self, *args, **kwargs):
        context = super(CidadeUpdate, self).get_context_data(*args, **kwargs)
        context['titulo'] = "Editar cadastro de Cidade"
        context['botao'] = "Salvar"
        context['classeBotao'] = "btn-success"
        return context


class PessoaUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    group_required = u"Usuário"
    model = Pessoa
    template_name = "formulario.html"
    success_url = reverse_lazy("listar-pessoas")
    fields = ['nome', 'nascimento', 'email', 'cidade']

    # Método utilizado para enviar dados ao template
    def get_context_data(self, *args, **kwargs):
        context = super(PessoaUpdate, self).get_context_data(*args, **kwargs)
        context['titulo'] = "Editar cadastro de Usuário"
        context['botao'] = "Salvar"
        context['classeBotao'] = "btn-success"
        return context


class TipoEstacaoUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    group_required = u"Administrador"
    model = TipoEstacao
    template_name = "formulario.html"
    success_url = reverse_lazy("listar-tipo-estacao")
    fields = ['tipo']

    # Altera a query para buscar o objeto do usuário logado
    def get_object(self, queryset=None):
        self.object = get_object_or_404(
            TipoEstacao, pk=self.kwargs['pk'], usuario=self.request.user)
        return self.object

    # Método utilizado para enviar dados ao template
    def get_context_data(self, *args, **kwargs):
        context = super(TipoEstacaoUpdate, self).get_context_data(*args, **kwargs)
        context['titulo'] = "Editar de novos tipos de Estação"
        context['botao'] = "Salvar"
        context['classeBotao'] = "btn-primary"
        return context


class EstacaoUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    group_required = u"Usuário"
    model = Estacao
    template_name = "formulario.html"
    success_url = reverse_lazy("listar-estacao")
    fields = ['local', 'capacidade', 'cidade']

    # Altera a query para buscar o objeto do usuário logado
    def get_object(self, queryset=None):
        self.object = get_object_or_404(
            Estacao, pk=self.kwargs['pk'], usuario=self.request.user)
        return self.object

    # Método utilizado para enviar dados ao template
    def get_context_data(self, *args, **kwargs):
        context = super(EstacaoUpdate, self).get_context_data(*args, **kwargs)
        context['titulo'] = "Editar cadastro de ETA"
        context['botao'] = "Salvar"
        context['classeBotao'] = "btn-success"
        return context


class SensorUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    group_required = u"Usuário"
    model = Sensor
    template_name = "formulario.html"
    success_url = reverse_lazy("listar-sensor")
    fields = ['idsensor', 'tipo', 'estacao']

    # Altera a query para buscar o objeto do usuário logado
    def get_object(self, queryset=None):
        self.object = get_object_or_404(
            Sensor, pk=self.kwargs['pk'], usuario=self.request.user)
        return self.object

    # Método utilizado para enviar dados ao template
    def get_context_data(self, *args, **kwargs):
        context = super(SensorUpdate, self).get_context_data(*args, **kwargs)
        context['titulo'] = "Editar cadastro de Sensor"
        context['botao'] = "Salvar"
        context['classeBotao'] = "btn-primary"
        return context


class HistoricoConsumoUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    group_required = u"Usuário"
    model = HistoricoConsumo
    template_name = "formulario.html"
    success_url = reverse_lazy("listar-historico-consumo")
    fields = ['mes', 'ano', 'quantidade', 'valor']

    # Altera a query para buscar o objeto do usuário logado
    def get_object(self, queryset=None):
        self.object = get_object_or_404(
            HistoricoConsumo, pk=self.kwargs['pk'], usuario=self.request.user)
        return self.object

    # Método utilizado para enviar dados ao template
    def get_context_data(self, *args, **kwargs):
        context = super(HistoricoConsumoUpdate, self).get_context_data(*args, **kwargs)
        context['titulo'] = "Editar cadastro de Consumo"
        context['botao'] = "Salvar"
        context['classeBotao'] = "btn-primary"
        return context


##################### Excluir ######################


class EstadoDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    group_required = u"Administrador"
    # Define qual o modelo pra essa classe vai criar o form
    model = Estado
    # Qual o html que será utilizado?
    template_name = "formulario.html"
    # Pra onde redirecionar o usuário depois de excluir um registro. Informe o nome da url
    success_url = reverse_lazy("listar-estados")

    # Método utilizado para enviar dados ao template
    def get_context_data(self, *args, **kwargs):
        # Chamar o "pai" para que sempre tenha o comportamento padrão, além do nosso
        context = super(EstadoDelete, self).get_context_data(*args, **kwargs)

        # Adicionar coisas ao contexto que serão enviadas para o html
        context['titulo'] = "Deseja excluir esse registro?"
        context['botao'] = "Excluir"
        context['classeBotao'] = "btn-danger"

        # Devolve/envia o context para seu comportamento padrão
        return context


class CidadeDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    group_required = u"Administrador"
    model = Cidade
    template_name = "formulario.html"
    success_url = reverse_lazy("listar-cidades")

    def get_context_data(self, *args, **kwargs):
        context = super(CidadeDelete, self).get_context_data(*args, **kwargs)
        context['titulo'] = "Deseja excluir esse registro?"
        context['botao'] = "Excluir"
        context['classeBotao'] = "btn-danger"
        return context


class PessoaDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    group_required = u"Administrador"
    model = Pessoa
    template_name = "formulario.html"
    success_url = reverse_lazy("listar-pessoa")

    def get_context_data(self, *args, **kwargs):
        context = super(PessoaDelete, self).get_context_data(*args, **kwargs)
        context['titulo'] = "Deseja excluir esse registro?"
        context['botao'] = "Excluir"
        context['classeBotao'] = "btn-danger"
        return context


class TipoEstacaoDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    group_required = u"Administrador"
    model = TipoEstacao
    template_name = "formulario.html"
    success_url = reverse_lazy("listar-tipo-estacao")

    # Altera a query para buscar o objeto do usuário logado
    def get_object(self, queryset=None):
        self.object = get_object_or_404(
            TipoEstacao, pk=self.kwargs['pk'], usuario=self.request.user)
        return self.object

    # Método utilizado para enviar dados ao template
    def get_context_data(self, *args, **kwargs):
        context = super(TipoEstacaoDelete, self).get_context_data(*args, **kwargs)
        context['titulo'] = "Deseja excluir esse registro?"
        context['botao'] = "Excluir"
        context['classeBotao'] = "btn-primary"
        return context


class EstacaoDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    group_required = u"Usuário"
    model = Estacao
    template_name = "formulario.html"
    success_url = reverse_lazy("listar-estacao")

    # Altera a query para buscar o objeto do usuário logado
    def get_object(self, queryset=None):
        self.object = get_object_or_404(
            Estacao, pk=self.kwargs['pk'], usuario=self.request.user)
        return self.object

    def get_context_data(self, *args, **kwargs):
        context = super(EstacaoDelete, self).get_context_data(*args, **kwargs)
        context['titulo'] = "Deseja excluir esse registro?"
        context['botao'] = "Excluir"
        context['classeBotao'] = "btn-danger"
        return context


class SensorDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    group_required = u"Usuário"
    model = Sensor
    template_name = "formulario.html"
    success_url = reverse_lazy("listar-sensor")

    # Altera a query para buscar o objeto do usuário logado
    def get_object(self, queryset=None):
        self.object = get_object_or_404(
            Sensor, pk=self.kwargs['pk'], usuario=self.request.user)
        return self.object

    # Método utilizado para enviar dados ao template
    def get_context_data(self, *args, **kwargs):
        context = super(SensorDelete, self).get_context_data(*args, **kwargs)
        context['titulo'] = "Deseja excluir esse registro?"
        context['botao'] = "Excluir"
        context['classeBotao'] = "btn-primary"
        return context


class HistoricoConsumoDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    group_required = u"Usuário"
    model = HistoricoConsumo
    template_name = "formulario.html"
    success_url = reverse_lazy("listar-historico-consumo")

    # Altera a query para buscar o objeto do usuário logado
    def get_object(self, queryset=None):
        self.object = get_object_or_404(
            HistoricoConsumo, pk=self.kwargs['pk'], usuario=self.request.user)
        return self.object

    # Método utilizado para enviar dados ao template
    def get_context_data(self, *args, **kwargs):
        context = super(HistoricoConsumoDelete, self).get_context_data(*args, **kwargs)
        context['titulo'] = "Deseja excluir esse registro?"
        context['botao'] = "Excluir"
        context['classeBotao'] = "btn-primary"
        return context


##################### Listar ######################

# Vai gerar uma tela com uma lista de estados


class EstadoList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    group_required = u"Usuário"
    # Inform qual o modelo
    model = Estado
    # E o template
    template_name = "listas/list_estado.html"


class CidadeList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    group_required = u"Usuário"
    model = Cidade
    template_name = "listas/list_cidade.html"


class PessoaList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    group_required = u"Administrador"
    model = Pessoa
    template_name = "listas/list_pessoa.html"


class TipoEstacaoList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    group_required = u"Usuário"
    model = Sensor
    template_name = "listas/list_tipo_estacao.html"

    # Altera a query padrão para buscar somente dados do usuário logado
    def get_queryset(self):
        # O object_list é o nome padrão para armazenar uma lista de objetos de um ListView
        self.object_list = TipoEstacao.objects.filter(usuario=self.request.user)
        return self.object_list


class EstacaoList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    group_required = u"Usuário"
    model = Estacao
    template_name = "listas/list_estacao.html"

    # Altera a query padrão para buscar somente dados do usuário logado
    def get_queryset(self):
        # O object_list é o nome padrão para armazenar uma lista de objetos de um ListView
        self.object_list = Estacao.objects.filter(usuario=self.request.user)
        return self.object_list


class SensorList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    group_required = u"Usuário"
    model = Sensor
    template_name = "listas/list_sensor.html"

    # Altera a query padrão para buscar somente dados do usuário logado
    def get_queryset(self):
        # O object_list é o nome padrão para armazenar uma lista de objetos de um ListView
        self.object_list = Sensor.objects.filter(usuario=self.request.user)
        return self.object_list


class HistoricoConsumoList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    group_required = u"Usuário"
    model = HistoricoConsumo
    template_name = "listas/list_historico_consumo.html"

    # Altera a query padrão para buscar somente dados do usuário logado
    def get_queryset(self):
        # O object_list é o nome padrão para armazenar uma lista de objetos de um ListView
        self.object_list = HistoricoConsumo.objects.filter(usuario=self.request.user)
        return self.object_list
