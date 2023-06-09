@echo off

python manage.py check --deploy
python manage.py collectstatic --noinput
python manage.py migrate --no-input
python manage.py seed_data --skip-checks
start python manage.py rqworker --with-scheduler
start python manage.py crontab add
gunicorn bank_project.asgi:application -b 0.0.0.0:8000 -k uvicorn.workers.UvicornWorker