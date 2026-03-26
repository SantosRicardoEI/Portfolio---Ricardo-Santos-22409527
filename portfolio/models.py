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

# Representa uma unidade curricular em abstrato
class UnidadeCurricular(models.Model):
    nome = models.CharField(max_length=150)
    sigla = models.CharField(max_length=20, blank=True)
    descricao = models.TextField(blank=True)
    ects = models.DecimalField(max_digits=4, decimal_places=1, null=True, blank=True)
    imagem = models.ImageField(upload_to='ucs/', blank=True, null=True)

    def __str__(self):
        return self.nome


# Representa a oferta de uma UC num certo curso e ano letivo
class OfertaUC(models.Model):
    unidade_curricular = models.ForeignKey(
        UnidadeCurricular,
        on_delete=models.CASCADE,
        related_name='ofertas'
    )
    curso = models.ForeignKey(
        Curso,
        on_delete=models.CASCADE,
        related_name='ofertas_uc'
    )
    ano_letivo = models.ForeignKey(
        AnoLetivo,
        on_delete=models.CASCADE,
        related_name='ofertas_uc'
    )
    docentes = models.ManyToManyField(
        'Professor',
        related_name='ofertas_uc',
        blank=True
    )

    def __str__(self):
        return f"{self.unidade_curricular.nome} - {self.curso.nome} - {self.ano_letivo.nome}"
    
# Representa uma tecnologia
class Tecnologia(models.Model):
    CATEGORIAS = [
        ('linguagem', 'Linguagem'),
        ('framework', 'Framework'),
        ('bd', 'Base de Dados'),
        ('ferramenta', 'Ferramenta'),
        ('outro', 'Outro'),
    ]

    nome = models.CharField(max_length=100, unique=True)
    descricao = models.TextField(blank=True)
    categoria = models.CharField(max_length=20, choices=CATEGORIAS)
    logo = models.ImageField(upload_to='tecnologias/', blank=True, null=True)
    website_oficial = models.URLField(blank=True, null=True)
    nivel_interesse = models.PositiveIntegerField(default=3)

    def __str__(self):
        return self.nome
    
# Representa uma área
class Area(models.Model):
    nome = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nome


# Representa uma palavra-chave
class PalavraChave(models.Model):
    nome = models.CharField(max_length=100, unique=True)

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