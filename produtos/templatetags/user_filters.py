from django.template import Library

from utils.formatar_preco import formatar_preco
from utils.total_carrinho import carrinho_total_qtd

register = Library()


@register.filter
def formata_preco(val):
    return formatar_preco(val)


@register.filter
def total_carrinho(carrinho):
    return carrinho_total_qtd(carrinho)
