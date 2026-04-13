from django.db import models

from utils.formatar_preco import formatar_preco
from utils.resimensiona_imagem import redimensiona_imagem

from .utils.rands import slugify_new


class Produto(models.Model):
    nome = models.CharField(max_length=255)
    categoria = models.CharField(max_length=255, default='Geral')
    descricao_curta = models.TextField(max_length=255)
    descricao_longa = models.TextField()
    imagem = models.ImageField(
        upload_to='produtos_imagens/%Y/%m/', blank=True, null=True
    )
    slug = models.SlugField(unique=True, blank=True, null=True)
    preco_marketing = models.FloatField()
    preco_marketing_promocional = models.FloatField(default=0)
    tipo = models.CharField(
        default='V',
        max_length=1,
        choices=(
            ('V', 'Variável'),
            ('S', 'Simples'),
        )
    )

    def get_preco_formatado(self):
        return formatar_preco(self.preco_marketing)

    def get_preco_promocional_formatado(self):
        return formatar_preco(self.preco_marketing_promocional)

    def save(self, *args, **kwargs):

        # TODO: Adicionar um método de criação de slug automático
        if not self.slug:
            self.slug = slugify_new(self.nome, 4)
        nome_imagem_atual = str(self.imagem.name)
        super_save = super().save(*args, **kwargs)
        imagem_mudou = False
        if self.imagem:
            imagem_mudou = nome_imagem_atual != self.imagem.name

        if imagem_mudou:
            redimensiona_imagem(self.imagem, 900)

        return super_save

    def __str__(self) -> str:
        return self.nome


class Variacao(models.Model):
    class Meta:
        verbose_name = 'Variação'
        verbose_name_plural = 'Variações'

    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    nome = models.CharField(max_length=50, blank=True, null=True)
    preco = models.FloatField()
    preco_promocional = models.FloatField(default=0)
    estoque = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.nome
