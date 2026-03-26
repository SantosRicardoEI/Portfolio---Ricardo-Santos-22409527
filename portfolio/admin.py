from django.contrib import admin
from .models import (
    Curso,
    AnoLetivo,
    Professor,
    MakingOf,
    EvidenciaMakingOf,
    UnidadeCurricular,
    OfertaUC,
    Tecnologia,
    Area,
    PalavraChave,
)

class EvidenciaMakingOfInline(admin.StackedInline):
    model = EvidenciaMakingOf
    extra = 1

@admin.register(MakingOf)
class MakingOfAdmin(admin.ModelAdmin):
    list_display = ('entidade', 'titulo', 'data_registo')
    search_fields = ('entidade', 'titulo', 'descricao_processo')
    list_filter = ('entidade', 'data_registo')
    inlines = [EvidenciaMakingOfInline]

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    search_fields = ('nome',)


@admin.register(AnoLetivo)
class AnoLetivoAdmin(admin.ModelAdmin):
    search_fields = ('nome',)


@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'pagina_pessoal')
    search_fields = ('nome', 'email')

@admin.register(UnidadeCurricular)
class UnidadeCurricularAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sigla', 'ects')
    search_fields = ('nome', 'sigla')


@admin.register(OfertaUC)
class OfertaUCAdmin(admin.ModelAdmin):
    list_display = ('unidade_curricular', 'curso', 'ano_letivo')
    list_filter = ('curso', 'ano_letivo')
    search_fields = ('unidade_curricular__nome', 'curso__nome')

@admin.register(Tecnologia)
class TecnologiaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'categoria', 'nivel_interesse')
    list_filter = ('categoria',)
    search_fields = ('nome',)


@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    search_fields = ('nome',)


@admin.register(PalavraChave)
class PalavraChaveAdmin(admin.ModelAdmin):
    search_fields = ('nome',)
