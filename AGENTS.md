# AGENTS.md - Django E-commerce Project

## Project Type
Django 6.0 e-commerce project (Python)

## Key Commands
```bash
python manage.py runserver      # Start dev server
python manage.py check          # Verify config
python manage.py migrate        # Apply migrations
python manage.py shell          # Django shell
```

## URL Routing (Critical)
**URL order matters in Django.** Define specific routes BEFORE dynamic routes like `<slug>`.

Bad (causes 404):
```python
path('<slug>', ...),
path('adicionarcarrinho/', ...),
```

Correct:
```python
path('adicionarcarrinho/', ...),
path('<slug>', ...),
```

## App Structure
- `produtos/` - Product catalog, cart logic
- `perfil/` - User profiles  
- `pedidos/` - Orders
- `loja/` - Main project config

## Template URL Syntax
Use: `{% url 'app_name:url_name' %}` (with quotes inside template tag)

Example: `{% url 'produtos:adicionarcarrinho' %}`

## Verification Steps
After URL changes, always verify:
```bash
python manage.py check
python manage.py shell -c "from django.urls import reverse; print(reverse('produtos:adicionarcarrinho'))"
```

## Repo-Specific Quirks
- Cart data is stored in `request.session.carrinho`, no database Cart model.
- Custom CSS lives at `templates/static/assets/custom/css/style.css`; pure CSS does not support nested `:hover` (separate rule required, e.g., `.product-link:hover` instead of nesting inside `.product-link`).
- Custom template filters (e.g., `formata_preco`) require `{% load user_filters %}` in templates; filter code lives in app-level `templatetags/` directories.
- Base templates are in root `templates/`; app templates follow `app_name/templates/app_name/` convention.
