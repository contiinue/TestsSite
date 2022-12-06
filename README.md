
# Установка и запуск

``` git clone git@github.com:contiinue/test-task.git && cd test_task ```
___
## Установка с докером

### Необходимо создать .env файл и добавить переменные окружения
```
# Postgresql environments

POSTGRES_USER=postgres_user
POSTGRES_PASSWORD=postgres_password
POSTGRES_DB=postgres_db

# Django superuser
DJANGO_SUPERUSER_PASSWORD=test_password
DJANGO_SUPERUSER_EMAIL=root@root.com
DJANGO_SUPERUSER_USERNAME=root

# Django
DJANGO_SECRET_KEY='some_secret_key'
```

