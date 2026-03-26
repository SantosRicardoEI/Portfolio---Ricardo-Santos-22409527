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