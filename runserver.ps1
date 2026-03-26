Write-Host "📂 Coletando arquivos estáticos..." -ForegroundColor Cyan
python manage.py collectstatic --noinput

Write-Host "⚙️ Preparando as migrações..." -ForegroundColor Cyan
python manage.py makemigrations --noinput

Write-Host "🗄️ Aplicando as migrações..." -ForegroundColor Cyan
python manage.py migrate --noinput

Write-Host "🚀 Iniciando o servidor local..." -ForegroundColor Green
python manage.py runserver