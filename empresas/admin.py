from django.contrib import admin
from django.utils.html import format_html
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import Documento, Empresa

class DocumentoInline(admin.StackedInline):
    verbose_name = "Documento"
    model = Documento
    extra = 3

class EmpresaResource(resources.ModelResource):
    class Meta:
        model = Empresa
        exclude = ('id',)
        widgets = {
                'data_da_visita': {'format': '%d.%m.%Y'},
                }

class EmpresaAdmin(ImportExportModelAdmin):
    def indicado(self, obj):
        colors = {
            'S': 'green',
            'N': 'red'
        }
        return format_html(
        '<b style="color:{}; background:{}">{}</b>',
        colors[obj.indicado],
        colors[obj.indicado], 
        obj.indicado + obj.indicado,
    )
    list_display = ['razao_social', 'indicado', 'data_da_visita', 'briefing']
    list_filter = ('razao_social', 'data_da_visita')
    search_fields = ['razao_social', 'endereco']
    inlines = [DocumentoInline]
    resource_class = EmpresaResource


admin.site.register(Empresa, EmpresaAdmin)
admin.site.site_header = 'Controle de Visitas - GrupoGP'
admin.site.site_title = 'Sistema de Controle de Visitas'