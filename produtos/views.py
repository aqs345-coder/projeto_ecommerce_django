from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from django.views import View


class ListaProdutos(ListView):
    pass


class DetalheProduto(View):
    pass


class AdicionarCarrinho(View):
    pass


class RemoverCarrinho(View):
    pass


class Carrinho(View):
    pass


class Finalizar(View):
    pass
