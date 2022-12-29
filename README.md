# PROYECTO FINAL - INGENIERIA DE SOFTWARE II
## _TodoList - Django App_

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

Django-Todolist es una aplicación web de listas de tareas con las funciones más básicas de la mayoría de las aplicaciones web, es decir, cuentas/inicio de sesión, API y una interfaz de usuario algo interactiva.

Lista de tareas abarcadas por la modificacion del proyecto inicial:
- Pipeline
- Creacion de repositorio y branches correspondientes (Github): repositorio: [django_todolist](https://github.com/SamuelChambiYtusaca/django-todolist)
- Aplicacion de herramientas de construcción Automática (PyBuilder).
> Construcción automática: se separó la construcción de la ejecución de pruebas unitarias, las pruebas unitarias se realizan durante la ejecución del pipeline
![Error al cargar la imagen](https://github.com/SamuelChambiYtusaca/django-todolist/blob/willa/imagenes/build0.png)
![Error al cargar la imagen](https://github.com/SamuelChambiYtusaca/django-todolist/blob/willa/imagenes/build1.png)

- Análisis Estático (SonarQube).
> Issues encontrados usando la herramienta SonarQube
![Error al cargar la imagen](https://github.com/SamuelChambiYtusaca/django-todolist/blob/willa/imagenes/issue1.png)
![Error al cargar la imagen](https://github.com/SamuelChambiYtusaca/django-todolist/blob/willa/imagenes/issue2.png)
![Error al cargar la imagen](https://github.com/SamuelChambiYtusaca/django-todolist/blob/willa/imagenes/issue3.png)
![Error al cargar la imagen](https://github.com/SamuelChambiYtusaca/django-todolist/blob/willa/imagenes/issue4.png)
![Error al cargar la imagen](https://github.com/SamuelChambiYtusaca/django-todolist/blob/willa/imagenes/issue5.png)

> Security hotspot encontrado usando herramienta SonarQube
![Error al cargar la imagen](https://github.com/SamuelChambiYtusaca/django-todolist/blob/willa/imagenes/security_hotspot1.png)

- Pruebas Unitarias.
> Test 1: usert_tests
![Error al cargar la imagen](https://github.com/SamuelChambiYtusaca/django-todolist/blob/willa/imagenes/test1.png)
> Test 2: account_tests
![Error al cargar la imagen](https://github.com/SamuelChambiYtusaca/django-todolist/blob/willa/imagenes/test2.png)
> Test 3: list_model_tests
![Error al cargar la imagen](https://github.com/SamuelChambiYtusaca/django-todolist/blob/willa/imagenes/test3.png)
> Test 4: lists_tests
![Error al cargar la imagen](https://github.com/SamuelChambiYtusaca/django-todolist/blob/willa/imagenes/test4.png)
> Test 5: login_for_tests
![Error al cargar la imagen](https://github.com/SamuelChambiYtusaca/django-todolist/blob/willa/imagenes/test5.png)
> Test 6: todo_form_tests
![Error al cargar la imagen](https://github.com/SamuelChambiYtusaca/django-todolist/blob/willa/imagenes/test6.png)
> Test 7: todo_list_form_tests
![Error al cargar la imagen](https://github.com/SamuelChambiYtusaca/django-todolist/blob/willa/imagenes/test7.png)
> Test 8: todo_list_tests
![Error al cargar la imagen](https://github.com/SamuelChambiYtusaca/django-todolist/blob/willa/imagenes/test8.png)
> Test 9: todo_tests
![Error al cargar la imagen](https://github.com/SamuelChambiYtusaca/django-todolist/blob/willa/imagenes/test9.png)

- Pruebas Funcionales (Selenium Webdriver).
> Pruebas funcionales implementadas
![Error al cargar la imagen](https://github.com/SamuelChambiYtusaca/django-todolist/blob/willa/imagenes/pruebas_funcionales.png)

- Gestion de tareas e Issues (Trello).
> Tareas asignadas en Trello
![Error al cargar la imagen](https://github.com/SamuelChambiYtusaca/django-todolist/blob/willa/imagenes/trello.png)

# LABORATORIO 8
 - Documento de reporte de SonarQube y SonarLint: [lab 8 pdf](https://github.com/SamuelChambiYtusaca/django-todolist/blob/willa/Lab8_Reporte_SonarQube_Sonarlint.pdf)
 > Code smells encontrados usando la herramamienta SonarLint
![Error al cargar la imagen](https://github.com/SamuelChambiYtusaca/django-todolist/blob/willa/imagenes/code_smell1.png)
![Error al cargar la imagen](https://github.com/SamuelChambiYtusaca/django-todolist/blob/willa/imagenes/code_smell2.png)

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
