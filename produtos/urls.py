from django.urls import path

from . import views

app_name = 'produtos'

urlpatterns = [
    path('', views.ListaProdutos.as_view(), name='lista'),
    path('adicionarcarrinho/', views.AdicionarCarrinho.as_view(),
         name='adicionarcarrinho'),
    path('removercarrinho/', views.RemoverCarrinho.as_view(), name='removercarrinho'),
    path('carrinho/', views.Carrinho.as_view(), name='carrinho'),
    path('resumodacompra/', views.ResumoDaCompra.as_view(), name='resumodacompra'),
    path('<slug>', views.DetalheProduto.as_view(), name='detalhe'),
]
