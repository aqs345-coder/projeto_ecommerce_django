# 🛒 E-commerce Django

![Python Version](https://img.shields.io/badge/python-3.10+-blue.svg)
![Django Version](https://img.shields.io/badge/Django-6.0-092E20?style=flat&logo=django&logoColor=white)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

Uma plataforma de loja virtual completa, robusta e escalável desenvolvida com Django 6.0. Este projeto contempla desde a exibição dinâmica de produtos até o checkout, incluindo validações de dados brasileiros e gestão avançada de estoque.

## ✨ Funcionalidades

- **Catálogo Avançado:** Suporte para produtos simples e produtos com variações (tamanhos, cores, etc.).
- **Carrinho de Compras:** Sistema de adição, remoção e cálculo de totais integrado com a sessão do usuário.
- **Painel do Cliente:** Perfis individuais com validação real de dados (CPF) e preenchimento de endereço.
- **Gestão de Pedidos:** Fluxo completo de finalização de compra e acompanhamento de status.
- **Mock de Dados (Seed):** Geração de base de dados realista para testes de interface e paginação em ambiente de desenvolvimento.

## 🛠️ Tecnologias Utilizadas

**Back-end:**
- Python 3.10+
- Django 6.0
- SQLite3 (Banco de dados padrão)
- Faker (Geração de dados de teste)
- Pillow (Processamento e redimensionamento automático de imagens)

**Front-end:**
- HTML5 / CSS3 (Arquitetura orientada a Design Tokens e Flexbox)
- Bootstrap (Componentes de UI)

**Ferramentas:**
- Django Debug Toolbar (Otimização de queries SQL)

---

## 🚀 Como Executar o Projeto (Setup)

Siga as instruções abaixo para rodar o projeto no seu ambiente local.

### 1. Clonar o repositório
```bash
git clone [https://github.com/seu-usuario/nome-do-repositorio.git](https://github.com/seu-usuario/nome-do-repositorio.git)
cd nome-do-repositorio
```

### 2. Configurar o Ambiente Virtual
```bash
# Criar o ambiente virtual
python -m venv venv

# Ativar o ambiente (Linux/Mac)
source venv/bin/activate

# Ativar o ambiente (Windows)
venv\Scripts\activate
```

### 3. Instalar as Dependências
```bash
pip install -r requirements.txt
```

### 4. Configurar o Banco de Dados
```bash
# Executar as migrações estruturais
python manage.py migrate

# Criar um usuário administrador para acessar o painel
python manage.py createsuperuser
```

### 5. Iniciar o Servidor
```bash
python manage.py runserver
```
Acesse o painel do cliente em `http://127.0.0.1:8000/` ou o painel administrativo em `http://127.0.0.1:8000/admin/`.

---

## 🎲 Populando o Banco de Dados (Seed)

Para facilitar os testes de layout e navegação, este projeto possui um *Management Command* customizado que preenche o banco de dados com produtos, variações e preços realistas automaticamente.

Com o ambiente virtual ativado, basta rodar:
```bash
python manage.py seed
```

## 📂 Estrutura do Projeto

```text
projeto_ecommerce_django/
├── loja/               # Configurações globais (settings, urls principais)
├── produtos/           # App: Models de produtos, categorias e views de catálogo
├── perfil/             # App: Autenticação, perfis e validações (CPF/CEP)
├── pedidos/            # App: Lógica de carrinho, checkout e histórico
├── templates/          # Arquivos HTML base e layouts globais
└── utils/              # Funções utilitárias (formatação de preço, geradores de slug)
```

## 💻 Comandos Úteis (Dev)

```bash
python manage.py check          # Verifica problemas de configuração no projeto
python manage.py shell          # Abre o shell interativo do Django
python manage.py makemigrations # Prepara novas alterações do banco de dados
```

## 📄 Licença

Este projeto está sob a licença [MIT](https://choosealicense.com/licenses/mit/). Sinta-se livre para usá-lo e modificá-lo.
