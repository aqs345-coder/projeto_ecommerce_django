# E-commerce Django

Loja virtual construida com Django 6.0.

##Funcionalidades

- Catálogo de produtos com variações
- Carrinho de compras
- Perfil de usuário com validação de CPF e CEP
- Gestão de pedidos

##Tech Stack

- Python 3.10+
- Django 6.0
- Pillow (processamento de imagens)
- Django Debug Toolbar

##Setup

```bash
# Criar ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows

# Instalar dependências
pip install -r requirements.txt

# Criar banco de dados
python manage.py migrate

# Criar super usuário
python manage.py createsuperuser

# Executar servidor
python manage.py runserver
```

Acesse: http://127.0.0.1:8000/

## Estrutura do Projeto

```
projeto_ecommerce_django/
├── produtos/          # Catálogo de produtos
├── perfil/            # Perfis de usuário
├── pedidos/           # Gestão de pedidos
├── loja/              # Configurações do projeto
├── templates/         # Templates HTML
└── utils/             # Utilitários
```

## Comandos Úteis

```bash
python manage.py check          # Verificar configuração
python manage.py shell          # Abrir shell Django
python manage.py seed           # Popular banco com dados de teste
```

## Licença

MIT