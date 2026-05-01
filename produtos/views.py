from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from django.urls import reverse
from django.views import View
from django.views.generic import DetailView, ListView

from . import models


class ListaProdutos(ListView):
    model = models.Produto
    template_name = 'produtos/lista.html'
    context_object_name = 'produtos'
    paginate_by = 10


class DetalheProduto(DetailView):
    model = models.Produto
    template_name = 'produtos/detalhe.html'
    context_object_name = 'produto'
    slug_url_kwarg = 'slug'


class AdicionarCarrinho(View):
    def get(self, *args, **kwargs):
        http_referer = self.request.META.get(
            'HTTP_REFERER', reverse('produtos:lista'))
        variacao_id = self.request.GET.get('variacao_id')

        if not variacao_id:
            messages.error(
                self.request,
                'Produto não encontrado ou não existe.'
            )
            return redirect(http_referer)

        variacao = get_object_or_404(models.Variacao, id=variacao_id)

        if not self.request.session.get('carrinho'):
            self.request.session['carrinho'] = {}
            self.request.session.save()

        carrinho = self.request.session['carrinho']


class RemoverCarrinho(View):
    pass


class Carrinho(View):
    pass


class Finalizar(View):
    pass
