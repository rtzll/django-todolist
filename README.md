# Django-Todolist

[![License][license-image]][license-url] [![Build Status][travis-image]][travis-url]

Django-Todolist is a todolist web application with the most basic features of most web apps, i.e. accounts/login, API and (somewhat) interactive UI.

---
CSS | [Skeleton](http://getskeleton.com/)
JS  | [jQuery](https://jquery.com/)

A lot of the code is directly adapted from another project I did. Where I build a web app using Flask with the exact same premise as this project. Here the Flask version: https://github.com/0xfoo/flask-todolist


## Explore
To try out the app yourself install the requirements (works with Python 2 and 3)
```
pip install django djangorestframework
```
Migrate:
```
python manage.py migrate
```
And then start the server (default: http://localhost:8000)
```
python manage.py runserver
```

Now you can browse the API:
http://localhost:8000/api/

Or start on the landing page:
http://localhost:8000/


[license-url]: https://github.com/0xfoo/django-todolist/blob/master/LICENSE
[license-image]: https://img.shields.io/badge/license-MIT-blue.svg?style=flat

[travis-url]: https://travis-ci.org/0xfoo/django-todolist
[travis-image]: https://travis-ci.org/0xfoo/django-todolist.svg?branch=master
