# Django-Todolist
In this project I explored Django while writing a todolist web application with the most basic features of most web apps, i.e. accounts/login, API and (somewhat) interactive UI.

Using the Skeleton CSS framework I tried to achieve a look that is minimal and also modern. Opposed to a lot of small projects which are proof of concepty/exploratory I made a conscious effort to also build something that looks nice. Nonetheless I'm not a designer, so I strived for good enough.

A lot of the code here comes from another project I did. Where I build a web app using Flask with the exact same premise as this project. Here the Flask version: https://github.com/0xfoo/flask-todolist


### Explore
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


### Note
Currently some of the things that can be found in the Flask version are still missing.
I try to stay close to the idea, but will use whatever Django has to offer.

### License (MIT)
See LICENSE
