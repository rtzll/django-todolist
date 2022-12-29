# PROYECTO FINAL - INGENIERIA DE SOFTWARE II
## _TodoList - Django App_

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

Django-Todolist es una aplicación web de listas de tareas con las funciones más básicas de la mayoría de las aplicaciones web, es decir, cuentas/inicio de sesión, API y una interfaz de usuario algo interactiva.

Lista de tareas abarcadas por la modificacion del proyecto inicial:
- Creacion de repositorio y branches correspondientes (Github).
- Aplicacion de herramientas de construcción Automática (PyBuilder).
- Análisis Estático (SonarQube).
- Pruebas Unitarias ().
- Pruebas Funcionales (Selenium Webdriver).
- Gestion de tareas e Issues (Trello).


## Creacion del repositorio

## Instalacion de la aplicacion
- En una primera instancia, corremos el siguiente comando para la descarga de los requimientos.

        cd django-todolist
        pip install -r requirements.txt

- Continuamos con Migrate:

        python manage.py migrate
        
- Finalmente, iniciamos el servidor con:
        
        python manage.py runserver


# Django-Todolist

[![License][license-image]][license-url] [![Build Status][travis-image]][travis-url]

Django-Todolist is a todolist web application with the most basic features of most web apps, i.e. accounts/login, API and (somewhat) interactive UI.

---
CSS | [Skeleton](http://getskeleton.com/)
JS  | [jQuery](https://jquery.com/)

I've also build a quite similar app in Flask: https://github.com/rtzll/flask-todolist


## Explore
Try it out by installing the requirements. (Works only with python >= 3.8, due to Django 4)

    pip install -r requirements.txt

Migrate:

    python manage.py migrate

And then start the server (default: http://localhost:8000)

    python manage.py runserver


Now you can browse the [API](http://localhost:8000/api/)
or start on the [landing page](http://localhost:8000/)


[license-url]: https://github.com/rtzll/django-todolist/blob/master/LICENSE
[license-image]: https://img.shields.io/badge/license-MIT-blue.svg?style=flat

[travis-url]: https://travis-ci.org/rtzll/django-todolist
[travis-image]: https://travis-ci.org/rtzll/django-todolist.svg?branch=master
