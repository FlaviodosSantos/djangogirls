* link do tutorial djangogirls * <https://tutorial.djangogirls.org/pt/django_installation/>

## Instalação do ambiente e esqueleto do projeto django

1. Criar o diretório e entrar
```
    mkdir django
    cd django
```

2. Criar a venv 
```
    python -m venv venv    
```

3. Ativar a venv
``` 
    venv\Scripts\activate
```

4. Atualizar o pip
```
    python -m pip install upgrade pip
```

5. Instalar a ultima versão do django
```
    pip install django
```

6. Criar o projeto django
```
    django-admin startporject mysite .
```

7. Criar o app
```
    python manage.py startapp blog    
```

8. Alterar settings.py, acrecentar o app
```
    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'blog',
    ]
```

8.1. Alterar settings.py
```
    LANGUAGE_CODE = 'pt-br'
    TIME_ZONE = 'America/Sao_Paulo'

    STATIC_URL = '/static/'
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')
```

8.2. Alterar ALLOWED_HOSTS no settings.py para posteriormente deploy no PythonAnywhere.com
```
    ALLOWED_HOSTS = ['127.0.0.1', '.pythonanywhere.com']  
```

9. Criar o banco de dados
```
    python manage.py migrate
```
10. Ative o servidor e acesse o localhost:8000
```
    python manage.py migrate
```