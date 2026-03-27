from django.contrib import admin
from .utils.helpers import formata_preco
from .models import Produto, Variacao


class VariacaoInline(admin.TabularInline):
    model = Variacao
    extra = 1


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = [
        'nome', 'descricao_curta', 'preco_formatado', 'preco_promo_formatado',
    ]
    inlines = [
        VariacaoInline
    ]

    @admin.display(description='Preço')
    def preco_formatado(self, obj):
        return formata_preco(obj.preco_marketing)

    @admin.display(description='Preço Promo.')
    def preco_promo_formatado(self, obj):
        return formata_preco(obj.preco_marketing_promocional)


admin.site.register(Variacao)
