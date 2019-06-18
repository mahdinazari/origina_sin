# Writing your first Django app

### Install django

### Creating a project
You can create a `django` project with following commands:
```
$ django-admin startproject [PROJECT_NAME]
```
##### Let’s look at what startproject created:
```
[PROJECT_NAME]
    manage.py
    mysite/
        __init__.py
        settings.py
        urls.py
        wsgi.py
```
### Creating the Polls app
 We’ll create our poll app right next to your manage.py file so that it can be imported as its own top-level module, rather than a submodule of `[PROJECT_NAME]`.
To create your app, make sure you’re in the same directory as manage.py and type this command:
```
$ python manage.py startapp polls
```
That’ll create a directory polls, which is laid out like this:
```
polls/
    __init__.py
    admin.py
    apps.py
    migrations/
        __init__.py
    models.py
    tests.py
    views.py
```
### The development server
Let’s verify your Django project works. Change into the outer mysite directory, if you haven’t already, and run the following commands:
```
$ python manage.py runserver
```
