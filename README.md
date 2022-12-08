
# Установка и запуск

``` git clone git@github.com:contiinue/TestsSite.git && cd test_task ```

___
## Установка без докера

### Создать виртуальное окружение
```
python3.10 -m venv env
. env/bin/activate

```

### Необходимо создать базу данных или изменит DATABASES в TestsSite/settings.py 

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'yourdatabasename.db'),
    }
}
```

### Необходимо создать set_env.sh файл и добавить переменные окружения
```
export POSTGRES_DATABASE=
export POSTGRES_USER=
export POSTGRES_PASSWORD=
export POSTGRES_HOST=
export DJANGO_SECRET_KEY="some_secret_key"
#Django
DJANGO_SECRET_KEY='some_secret_key'
```

### Установка зависимостей
```
cd docker
python -m pip install -r requirements.txt
```

### Запуск
```
python manage.py runserver 8000
```
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
## Запуск
```
docker-compose up --build
```

