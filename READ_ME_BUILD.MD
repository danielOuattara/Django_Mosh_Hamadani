# Project

## Setting up your development environment

- install/update `Python` to the last version
  
- in the case of using `Python3` is is recommended to install `pip3`
  to handle packages.

- install `pipenv` to handle efficiently virtual environment when working on Python project.
  To do so run `pip3 install pipenv` or `sudo aptitude install pipenv`

- use of `VS Code` for this project
  
- install `Python` extension in `VS Code`

##  Creating Your First Django Project

- `mkdir storefront-app && cd storefront-app`
  
- `pipenv install django`
  
- Notice that `pipenv` first automatically install a virtual environment at some other place
  `/~/.local/share/virtualenvs/storefront-app-uZpJkKS1` and then install `Django` as requested

```bash
daniel@debian-dbo:~/Documents/Computing/Python_DJANGO/Django_Mosh_Hamadani/storefront-app$ pipenv install Django

Creating a virtualenv for this project...
Pipfile: /home/daniel/Documents/Computing/Python_DJANGO/Django_Mosh_Hamadani/storefront-app/Pipfile
Using /usr/bin/python3 (3.11.2) to create virtualenv...
⠼ Creating virtual environment...created virtual environment CPython3.11.2.final.0-64 in 305ms
  creator CPython3Posix(dest=/home/daniel/.local/share/virtualenvs/storefront-app-uZpJkKS1, clear=False, no_vcs_ignore=False, global=False)
  seeder FromAppData(download=False, pip=bundle, setuptools=bundle, wheel=bundle, via=copy, app_data_dir=/home/daniel/.local/share/virtualenv)
    added seed packages: pip==23.0.1, setuptools==66.1.1, wheel==0.38.4
  activators BashActivator,CShellActivator,FishActivator,NushellActivator,PowerShellActivator,PythonActivator

✔ Successfully created virtual environment!
Virtualenv location: /home/daniel/.local/share/virtualenvs/storefront-app-uZpJkKS1
Creating a Pipfile for this project...
Installing Django...
Pipfile.lock not found, creating...
Locking [packages] dependencies...
Locking [dev-packages] dependencies...
Updated Pipfile.lock (af42abefb766e975f7680f10368735353569fb4fe0114e59496a7202658362fc)!
Installing dependencies from Pipfile.lock (8362fc)...
To activate this project's virtualenv, run pipenv shell.
Alternatively, run a command inside the virtualenv with pipenv run.
daniel@debian-dbo:~/Documents/Computing/Python_DJANGO/Django_Mosh_Hamadani/storefront-app$ ^C
daniel@debian-dbo:~/Documents/Computing/Python_DJANGO/Django_Mosh_Hamadani/storefront-app$
```

- check `Django` installed, run : `pip3 freeze`
  
- `pipenv` also created two files in the current project directory: `Pipfile` and `Pipfile.lock`
  
- Open VS Code in the current project folder and inspect these files
  
- `Pipfile` is the equivalent of `package.json` in `npm Javascript` based projects
  
- `Pipfile.lock` is the equivalent of `package-lock.json` in `npm Javascript` based projects

- Then activate the virtual environment just created for the current project: run `pipenv shell`

```bash
daniel@debian-dbo:~/Documents/Computing/Python_DJANGO/Django_Mosh_Hamadani/storefront-app$ pipenv shell
Launching subshell in virtual environment...
 . /home/daniel/.local/share/virtualenvs/storefront-app-uZpJkKS1/bin/activate
daniel@debian-dbo:~/Documents/Computing/Python_DJANGO/Django_Mosh_Hamadani/storefront-app$  . /home/daniel/.local/share/virtualenvs/storefront-app-uZpJkKS1/bin/activate
(storefront-app) daniel@debian-dbo:~/Documents/Computing/Python_DJANGO/Django_Mosh_Hamadani/storefront-app$ 
```

- run `django-admin` only to see all the commands available from this utility.
  
- create a new Django project: `django-admin startproject storefront .`
  
**Note :** The period `.` at the end of the command requests Django to create the new
  project in the current directory, not in a new directory having the same name

- the global tree design looks like this:

```bash
├── db.sqlite3
├── manage.py
├── Pipfile
├── Pipfile.lock
└── storefront/
    ├── asgi.py
    ├── __init__.py
    ├── __pycache__
    ├── settings.py
    ├── urls.py
    └── wsgi.py
```

**Note :** After the project is created, we can see `manage.py` as a wrapper
around `django-admin` which takes the settings of this project into account
instead of `django-admin`. To understand it run `django-admin` to see all the
commands available. Then run `django-admin runserver` and see the error, telling
that `django-admin` at this point don't know the settings of the project.
Instead run `python3 manage.py` to see all the commands available from this utility

- At this stage, to start the project with no error: `python3 manage.py runserver [port]`

```bash
(storefront-app) daniel@debian-dbo:~/Documents/Computing/Python_DJANGO/Django_Mosh_Hamadani/storefront-app$ python3 manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).

You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
May 04, 2024 - 13:20:19
Django version 5.0.4, using settings 'storefront.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

##  Using the integrated Terminal in VS Code

- configure it properly to use python interpreter !!!
  
- find the path where the virtual environment is installed: `pipenv --venv` and copy it.

```bash
daniel@debian-dbo:~/Documents/Computing/Python_DJANGO/Django_Mosh_Hamadani/storefront-app$ pipenv --venv

/home/daniel/.local/share/virtualenvs/storefront-app-uZpJkKS1
daniel@debian-dbo:~/Documents/Computing/Python_DJANGO/Django_Mosh_Hamadani/storefront-app$
```

- into VS Code run `Ctrl + Shift + P` to open settings and type:  `Python: select intepreter`
  
- Then when asked, type in the path of the virtual env location + python exact location:
  `/home/daniel/.local/share/virtualenvs/storefront-app-uZpJkKS1/bin/python` + `hit Enter`

- Then open the integrated VS Code terminal, and notice that VS Code automatically activate
  the virtual environment:

```bash
source /home/daniel/.local/share/virtualenvs/storefront-app-uZpJkKS1/bin/activate
daniel@debian-dbo:~/Documents/Computing/Python_DJANGO/Django_Mosh_Hamadani/storefront-app$ source /home/daniel/.local/share/virtualenvs/storefront-app-uZpJkKS1/bin/activate
(storefront-app) daniel@debian-dbo:~/Documents/Computing/Python_DJANGO/Django_Mosh_Hamadani/storefront-app$ 
```

- Then start again the server in the completed correct virtual environment using the correct
  interpreter: `python3 manage.py runserver`

## Creating Your first Project

- Every Django project is made of many apps.
  
- explore and inspect the `/storefront-app/storefront/settings.py` file, specially
  the `INSTALLED_APPS` list to see the default apps that come up with any new Django
  boiler plate project

- open a new terminal on the same project root
  
- **start a new app**: run `python3 manage.py startapp playground`.

- A new folder called `playground` is created next to `storefront`
  
- Every Django app has the same structure

```bash
└── storefront-app
├── db.sqlite3
├── manage.py
├── Pipfile
├── Pipfile.lock
├── playground/
│   ├── admin.py # module to define the admin interface regarding this app
│   ├── apps.py  # module to configure the app
│   ├── __init__.py
│   ├── migrations/ # table for generating database table
│   ├── models.py # module to define the models for this app linked to database
│   ├── tests.py # module to handle test
│   └── views.py # module to handle requests
├── README.MD
└── storefront/
    ├── asgi.py
    ├── __init__.py
    ├── __pycache__/
    ├── settings.py
    ├── urls.py
    └── wsgi.py
```

- explore file and folder in `/storefront-app/playground/` folder [24 minutes]
  
- then register the newly started app `playground` in the `storefront-app/storefront/settings.py`

```py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'playground' #<---
]

```

##  Writing Views (request handlers)

- add a new view (request handler) function in `storefront-app/playground/views.py`

```py
def say_hello(request):
    """
    Here we can do anything that is backend logic:
    - CRUD from a database
    - send email
    - etc...
    """
    return HttpResponse("Hello Django world")

```

##  Mapping URLs to Views

- you want a response when sending a request to  `http://localhost:8000/playground/hello`
  
- create the module `storefront-app/playground/urls.py`
  
- add the following content:

```py
from django.urls import path
from . import views

'''
Docs:
- urlpatterns = URLConf module
- every app can have its own url app configuration
- we need to import URLConf from this app into to the main URLConf
'''
urlpatterns = [
path("hello/", views.say_hello)
]
```

- in `storefront-app/storefront/urls.py` module include the `storefront-app/playground/urls.py`

```py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('playground/', include('playground.urls')),
]

```

- make a `GET` request to `http://localhost:8000/playground/hello`

## Using Templates

- create the folder `storefront-app/playground/templates/`
  
- create the file: `storefront-app/playground/templates/hello.html`

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Hello</title>
  </head>
  <body>
    <h1>Hello Django world</h1>
  </body>
</html>
```

- update `storefront-app/playground/views.py` as follow:

```py
from django.shortcuts import render
from django.http import HttpResponse

def say_hello(request):
    # return HttpResponse("Hello Django world")
    return render(request, 'hello.html')
```

- make a `GET` request to `http://localhost:8000/playground/hello/` and see the response

- update again `storefront-app/playground/views.py` to :

```py
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# a view :  request --> response
# requests handler


def say_hello(request):

    # return HttpResponse("Hello Django world")

    # -> update to render hello.html
    # return render(request, 'hello.html')

    # -> update to include a context while rendering hello.html
    return render(
        request,
        template_name='hello.html',
        context={"name": "John Doe", "country": "China"})
```

- update again `storefront-app/playground/templates/hello.html` to use the `context` dictionary:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Hello</title>
  </head>
  <body>
    <h1>Hello Django world</h1>

    {% if name %}

    <h2>The context show {{name}} as user</h2>
    <p>{{name}} was born in {{country}}</p>

    {% else %}

    <h2>The context is not provided</h2>

    {% endif %}
  </body>
</html>

  ```

## Debugging Django Application in VS Code

- click on the debug button.
  
- click to create a `launch.json`

- select the application to work with, if many applications open at the same time.

- answer all the questions

- locate the `manage.py` for the application to debug

- locate the `launch.json` as follow to run on port `9000`:

```json
  {
  // Use IntelliSense to learn about possible attributes.
  // Hover to view descriptions of existing attributes.
  // For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Python Debugger: Django",
      "type": "debugpy",
      "request": "launch",
      "args": ["runserver", "9000"],
      "django": true,
      "autoStartBrowser": false,
      "program": "${workspaceFolder}/storefront-app/manage.py"
    }
  ]

}

```

- update as follow:

```python
def say_hello(request):
    """
    Here we can do anything backend logic:
    - CRUD from a database
    - send email
    - etc...
    """
    # return HttpResponse("Hello Django world")

    # -> update to render hello.html
    # return render(request, 'hello.html')

    # -> update to include a context while rendering hello.html

    """Starting debugging here"""
    x = 1
    y = 2
    return render(
        request,
        template_name='hello.html',
        context={"name": "John Doe", "country": "China"})

```

- add break point in front of `x = 1`

- start the server if not started

- navigate to `127.0.0.1:9000/playground/hello`

- click on `step over` `f10` to continue the flow of debugging

- one again update `storefront-app/playground/views.py`as follow:

```python
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# a view :  request --> response
# requests handler


def calculate():
    x = 1
    y = 2
    return x


def say_hello(request):
    """
    Here we can do anything backend logic:
    - CRUD from a database
    - send email
    - etc...
    """
    # return HttpResponse("Hello Django world")

    # -> update to render hello.html
    # return render(request, 'hello.html')

    # -> update to include a context while rendering hello.html

    """Starting debugging here"""

    x = calculate()
    return render(
        request,
        template_name='hello.html',
        context={"name": "John Doe", "country": "China"})

```

- place a breakpoint at `x = calculate()`

- then `step into` to see what happens in the calculate function
  
- remove the breakpoint(s) upon finish

##  Using Django Debug Toolbar

- search any browser for `django debug toolbar`
  
- install it : `python -m pip install django-debug-toolbar` OR `pipenv install django-debug-toolbar`

- read the documentation for the configuration from at:
  `https://django-debug-toolbar.readthedocs.io/en/latest/installation.html`

## Introduction to data modeling

- is always the first step.
  
- Relations: one-to-one, one-to-many, many-to-many

- Product:

```bash
Product:
  title
  description
  price
  inventory 
```

- Collection:

```bash
Product:
  title
  products
```

## Building an e-commerce data model

- let's build 5 entities and their relations

- Product*_______*Cart through CartItem as junction table

- Customer 1_______*Order

- Product*_______*Order through OrderItem as junction table

- Product*_______*Tag through TagItem as junction table

## Organizing models in apps

- each app has its own data model

- avoid monolithic app
  
- do **ONE** thing and do it **WELL**

- avoid breaking each entities into separate apps: it leads to too much
  coupled entities, also maintenance will be hard

- we get this architecture:

```bash
store (app)
  Product
  Collection
  Customer
  Cart
  CartItem
  Order
  OrderItem

# 

tags (app)
  Tag
  TaggedItem
```

- so each app is self-contained and provide a single piece of functionality
  
- create two new app `store` and `tags`
  
- update the `INSTALLED_APP` list in `storefront-app/storefront/settings.py`

### end of video @ 01h02'35"

## Coding model classes
