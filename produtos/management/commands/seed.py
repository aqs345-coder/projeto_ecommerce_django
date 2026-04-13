import random

from django.core.management.base import BaseCommand
from faker import Faker

from produtos.models import Produto, Variacao


class Command(BaseCommand):
    help = 'Popula o banco de dados com Produtos e Variações falsas'

    def handle(self, *args, **kwargs):
        fake = Faker('pt_BR')
        quantidade_produtos = 30  # Defina quantos produtos quer gerar

        self.stdout.write(self.style.WARNING(
            f'Gerando {quantidade_produtos} produtos e suas variações...'))

        categorias_exemplo = ['Suspensão', 'Motor',
                              'Chassi', 'Aerodinâmica', 'Freios', 'Eletrônica']
        tamanhos = ['P', 'M', 'G', 'GG']
        cores = ['Preto', 'Vermelho', 'Amarelo', 'Fibra de Carbono']

        for i in range(quantidade_produtos):
            # 1. Defina listas com vocabulário real do seu projeto
            nomes_pecas = [
                'Amortecedor', 'Disco de Freio', 'Módulo de Injeção',
                'Aerofólio Traseiro', 'Bandeja de Suspensão', 'Cubo de Roda',
                'Caixa de Direção', 'Sensor de Telemetria', 'Bateria de Lítio',
                'Cinto de Segurança 5 Pontos', 'Volante F1'
            ]

            adjetivos = ['Pro', 'Evo', 'Racing',
                         'Advanced', 'Ultra-light', 'Forged']

            descricoes_curtas = [
                "Peça de alta performance usinada em alumínio naval, garantindo leveza e resistência extrema.",
                "Desenvolvido em túnel de vento para maximizar o downforce e estabilidade do chassi.",
                "Componente eletrônico de alta precisão para leitura de dados em tempo real na pista.",
                "Estrutura reforçada em fibra de carbono, ideal para redução de peso não suspenso.",
                "Sistema homologado pelas normas SAE para máxima segurança do piloto."
            ]

            # 2. Monte os textos sorteando das listas
            nome_gerado = f"{random.choice(nomes_pecas)} {random.choice(adjetivos)} de Competição"
            descricao_gerada = f"{random.choice(descricoes_curtas)} O melhor custo-benefício para a sua equipe."

            # Preços
            preco_base = round(random.uniform(50.0, 3000.0), 2)
            tem_promocao = random.random() < 0.3
            preco_promo = round(preco_base * 0.8, 2) if tem_promocao else 0
            tipo_produto = random.choice(['S', 'V'])

            # 3. Crie o produto com os textos reais
            produto = Produto(
                nome=nome_gerado,
                categoria=random.choice(categorias_exemplo),
                descricao_curta=descricao_gerada,
                # Para a descrição longa, podemos repetir a curta e adicionar algo extra do Faker
                descricao_longa=f"{descricao_gerada} Este produto foi testado sob as mais rigorosas condições. Garantia de 1 ano contra defeitos de fabricação.",
                preco_marketing=preco_base,
                preco_marketing_promocional=preco_promo,
                tipo=tipo_produto,
                imagem='produtos_imagens/placeholder.png'
            )
            produto.save()  # Aqui o seu save() entra em ação e gera o slug

            # 3. Criando as Variações atreladas a este produto
            if tipo_produto == 'V':
                # Se for variável, cria de 2 a 4 variações
                qtd_variacoes = random.randint(2, 4)

                # Escolhe aleatoriamente se a variação será por cor ou tamanho
                tipo_nome_variacao = random.choice([tamanhos, cores])
                nomes_escolhidos = random.sample(
                    tipo_nome_variacao, k=qtd_variacoes)

                for nome_var in nomes_escolhidos:
                    # Pequena oscilação de preço entre as variações
                    acrescimo = round(random.uniform(0, 100.0), 2)

                    Variacao.objects.create(
                        produto=produto,
                        nome=nome_var,
                        preco=preco_base + acrescimo,
                        preco_promocional=(
                            preco_promo + acrescimo) if tem_promocao else 0,
                        estoque=random.randint(0, 20)
                    )
            else:
                # Se for simples, cria apenas 1 variação padrão genérica
                Variacao.objects.create(
                    produto=produto,
                    nome='Único',
                    preco=preco_base,
                    preco_promocional=preco_promo,
                    estoque=random.randint(5, 50)
                )

        self.stdout.write(self.style.SUCCESS(
            f'Sucesso! {quantidade_produtos} produtos criados.'))
