from django.db import models


# Representa um curso
class Curso(models.Model):
    nome = models.CharField(max_length=150)

    def __str__(self):
        return self.nome

# Representa um ano letivo
class AnoLetivo(models.Model):
    nome = models.CharField(max_length=9, unique=True)  # ex: 2025/2026

    def __str__(self):
        return self.nome
    
# Representa um professor
class Professor(models.Model):
    nome = models.CharField(max_length=150)
    pagina_pessoal = models.URLField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.nome
    
    
class MakingOf(models.Model):
    entidade = models.CharField(max_length=100) 
    titulo = models.CharField(max_length=150)
    descricao_processo = models.TextField()
    decisoes_tomadas = models.TextField(blank=True)
    erros_encontrados = models.TextField(blank=True)
    correcoes_realizadas = models.TextField(blank=True)
    justificacao_modelacao = models.TextField(blank=True)
    uso_ia = models.TextField(blank=True)
    data_registo = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.entidade} - {self.titulo}"

class EvidenciaMakingOf(models.Model):
    making_of = models.ForeignKey(
        MakingOf,
        on_delete=models.CASCADE,
        related_name='evidencias'
    )
    titulo = models.CharField(max_length=150)
    descricao = models.TextField(blank=True)
    ficheiro = models.FileField(upload_to='makingof/evidencias/')
    data_upload = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo