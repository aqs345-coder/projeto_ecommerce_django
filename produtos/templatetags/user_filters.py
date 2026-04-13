from django.template import Library

from utils.formatar_preco import formatar_preco

register = Library()


@register.filter
def formata_preco(val):
    return formatar_preco(val)
