# Django-Todolist

Django-Todolist is a todolist web application with the most basic features of
most web apps, i.e. accounts/login, API and (somewhat) interactive UI.

---

CSS | [Skeleton](http://getskeleton.com/) JS | [jQuery](https://jquery.com/)

I've also build a quite similar app in Flask:
https://github.com/rtzll/flask-todolist

## Explore

Try it out by installing the dependencies using
[uv](https://docs.astral.sh/uv/).

    uv sync

Migrate:

    uv run python manage.py migrate

And then start the server (default: http://localhost:8000)

    uv run python manage.py runserver

Now you can browse the [API](http://localhost:8000/api/) or start on the
[landing page](http://localhost:8000/)

## Tests

Run the full test suite:

    uv run python manage.py test

Run tests for a specific app:

    uv run python manage.py test api
    uv run python manage.py test lists
