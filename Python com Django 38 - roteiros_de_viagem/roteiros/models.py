from django.db import models

class Roteiro(models.Model):
    nome = models.CharField(max_length=100)
    data_inicio = models.DateField()
    data_fim = models.DateField()

    def __str__(self):
        return self.nome

class Destino(models.Model):
    nome = models.CharField(max_length=100)
    roteiro = models.ForeignKey(Roteiro, related_name='destinos', on_delete=models.CASCADE)
    descricao = models.TextField()

    def __str__(self):
        return self.nome

class PontoTuristico(models.Model):
    nome = models.CharField(max_length=100)
    roteiro = models.ForeignKey(Roteiro, related_name='pontos_turisticos', on_delete=models.CASCADE)
    descricao = models.TextField()

    def __str__(self):
        return self.nome

class Restaurante(models.Model):
    nome = models.CharField(max_length=100)
    roteiro = models.ForeignKey(Roteiro, related_name='restaurantes', on_delete=models.CASCADE)
    descricao = models.TextField()
    custo = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nome

class Atividade(models.Model):
    nome = models.CharField(max_length=100)
    roteiro = models.ForeignKey(Roteiro, related_name='atividades', on_delete=models.CASCADE)
    descricao = models.TextField()
    data_atividade = models.DateField()

    def __str__(self):
        return self.nome
