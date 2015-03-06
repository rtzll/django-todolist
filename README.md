# Django-Todolist
In this project I explored Django while writing a todolist web application with the most basic features of most web apps, i.e. accounts/login, API and (somewhat) interactive UI.

Using the Skeleton CSS framework I tried to achieve a look that is minimal and also modern. Opposed to a lot of small projects which are proof of concepty/exploratory I made a conscious effort to also build something that looks nice. Nonetheless I'm not a designer, so I strived for good enough.

A lot of the code here comes from another project I did. Where I build a web app using Flask with the exact same premise as this project. Here the Flask version: https://github.com/0xfoo/flask-todolist


### Explore
To try out the app yourself install the requirements (works on Python2 and Python3)
```
pip install django djangorestframework
```
And then start the server (default: http://localhost:8000)
```
python manage.py runserver
```

Now you can browse the API:
http://localhost:8000/api/


### Note
I'm currently working on this, so a lot of things that are found in the Flask version are still missing. As of know I'm not sure to which degree I'll copy the functionality or maybe deviate to do some other features, that haven been released in the Flask version.

### License (MIT)
See LICENSE
