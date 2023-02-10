# Blog FGA

## Introdução
 Blog desenvolvido na disciplina de Desenvolvimento de software UnB.

## Requisitos
Ter instalado:
- python 3
- pip
- Django 4.1.3

## Instruções

### Como executar


### Aplicação
1.  Entre no diretório blog e execute Execute as migrations.
  ~~~
  python3 manage.py makemigrations fga
  python3 manage.py migrate
  ~~~

2. Execute a aplicação:

  ~~~
  python3 manage.py runserver
  ~~~
  
    Acesse: http://127.0.0.1:8000

3. Criar usuário admin

  ~~~
  python3 manage.py createsuperuser
  ~~~


### Docker

 1. Construindo e subindo o serviço

  ~~~
  docker-compose up --build
  ~~~