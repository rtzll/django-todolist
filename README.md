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
![Error al cargar la imagen](https://github.com/SamuelChambiYtusaca/django-todolist/blob/willa/imagenes/pruebas_funcionales.png)
<img src="https://github.com/SamuelChambiYtusaca/django-todolist/blob/willa/imagenes/pruebas_funcionales.png" scale=50%/>
- Gestion de tareas e Issues (Trello).
![Error al cargar la imagen](https://github.com/SamuelChambiYtusaca/django-todolist/blob/willa/imagenes/trello.png)

## Creacion del repositorio

## Instalacion de la aplicacion
- En una primera instancia, corremos el siguiente comando para la descarga de los requimientos.

        cd django-todolist
        pip install -r requirements.txt

- Continuamos con Migrate:
- Luego se inicia en el servidor (default: http://localhost:8000)

        python manage.py migrate
        
- Finalmente, iniciamos el servidor con:
        
        python manage.py runserver
