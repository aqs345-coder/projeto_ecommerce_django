from django.template import Library

from utils.formatar_preco import formatar_preco
from utils.total_carrinho import carrinho_total_qtd
from utils.valor_total_carrinho import total_carrinho

register = Library()


@register.filter
def formata_preco(val):
    return formatar_preco(val)


@register.filter
def quantidade_total_carrinho(carrinho):
    return carrinho_total_qtd(carrinho)


@register.filter
def valor_total_carrinho(carrinho):
    return total_carrinho(carrinho)
