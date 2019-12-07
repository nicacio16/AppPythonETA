from django.db import models
from django.contrib.auth.models import User

class Estado(models.Model):
    sigla = models.CharField(max_length=2)
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.sigla + " - " + self.nome

class Cidade(models.Model):
    nome = models.CharField(max_length=50)

    estado = models.ForeignKey(Estado, on_delete=models.PROTECT)

    def __str__(self):
        return self.nome + " - " + self.estado.sigla


class TipoEstacao(models.Model):
    tipo = models.CharField(max_length=50, verbose_name="Tipo de Estação", help_text="Ex: Casa, Empresa, Casa de Campo.")
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return self.tipo


class Estacao(models.Model):
    local = models.CharField(max_length=50, verbose_name="Local da Estação", help_text="Ex: casa, empresa, casa de campo.")
    capacidade = models.IntegerField(default=0, null=True, help_text="Qual a capacidade do reservatório? Ex: 10.500 litros.")
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)
    
    cidade = models.ForeignKey(Cidade, on_delete=models.PROTECT)    
    tipo = models.ForeignKey(TipoEstacao, on_delete=models.PROTECT)
    

    def __str__(self):
        return "{} - {} - {}".format(self.local, self.cidade, self.capacidade)


class Pessoa(models.Model):
    nome = models.CharField(max_length=50, null=True,  verbose_name="Digite seu nome?")
    cpf = models.CharField(max_length=11, null=True,  verbose_name="Digite seu CPF?")
    nascimento = models.DateField(verbose_name='Data de nascimento', null=True )
    email = models.CharField(null=True, max_length=100)

    cidade = models.ForeignKey(Cidade, on_delete=models.PROTECT, null=True)

    usuario = models.OneToOneField(User, on_delete=models.PROTECT)

    def __str__(self):
        return "{} - {}/{} - {} - {}".format(self.nome, self.cpf, self.cidade.nome, self.estacao.local, self.estacao.capacidade)


class Sensor(models.Model):
    idsensor = models.CharField(max_length=50, verbose_name="Número de série", help_text="Ex: 1XXEDKE23")
    tipo = models.CharField(max_length=50, help_text="Qual tipo de sensor")

    estacao = models.ForeignKey(Estacao, on_delete=models.PROTECT)
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return "{} - {}/{}".format(self.idsensor, self.tipo, self.estacao)


class HistoricoConsumo(models.Model):
    mes = models.CharField(max_length=15, verbose_name="Mês", help_text="Ex: Janeiro")
    ano = models.CharField(max_length=4, null=True, help_text="Ex: 2018")
    quantidade = models.DecimalField(max_digits=15, decimal_places=0, null=True,help_text="18 m3")
    valor = models.DecimalField(max_digits=15, decimal_places=2, null=True, help_text="35,00")
    
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return "{} - {}/{}".format(self.mes, self.ano, self.quantidade, self.valor)

