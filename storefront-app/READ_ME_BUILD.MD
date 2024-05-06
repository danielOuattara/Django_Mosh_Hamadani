# Project

## Setting up your development environment

- install/update `Python` to the last version
- in the case of using `Python3` is is recommended to install `pip3`
  to handle packages.
- install `pipenv` to handle efficiently virtual environment when working on Python project. To do so run `pip3 install pipenv` or `sudo aptitude install pipenv`
- use of `VS Code` for this project
- install `Python` extension in `VS Code`

##  Creating Your First Django Project

- `mkdir storefront-app && cd storefront-app`
- `pipenv install Django`
- Notice that `pipenv` first automatically install a virtual environment at some other place in the `/~/.local/share/virtualenvs/storefront-app-uZpJkKS1`
  and then install `Django` as requested

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

- check `Django` installed: `pip3 freeze`
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

- create a new Django project: `django-admin startproject storefront .`
- Note: the period `.` at the end of the command requests Django to create the new project in the current directory, not in a new directory having the same name

- start the project: `python3 manage.py runserver [port]`

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
- find the path where the virtual environment is installed: `pipenv --venv`

```bash
  daniel@debian-dbo:~/Documents/Computing/Python_DJANGO/Django_Mosh_Hamadani/storefront-app$ pipenv --venv

/home/daniel/.local/share/virtualenvs/storefront-app-uZpJkKS1
daniel@debian-dbo:~/Documents/Computing/Python_DJANGO/Django_Mosh_Hamadani/storefront-app$
  ```

- int VS Code run `Ctrl + Shift + P` to open settings and type:  `Python: select intepreter`
- Then  when asked, type in the path of the virtual env location + python exact location: `/home/daniel/.local/share/virtualenvs/storefront-app-uZpJkKS1/bin/python`  + `hit Enter`

- Then open the integrated VS Code terminal, and notice that VS Code automatically activate the virtual environment:

```bash
source /home/daniel/.local/share/virtualenvs/storefront-app-uZpJkKS1/bin/activate
daniel@debian-dbo:~/Documents/Computing/Python_DJANGO/Django_Mosh_Hamadani/storefront-app$ source /home/daniel/.local/share/virtualenvs/storefront-app-uZpJkKS1/bin/activate
(storefront-app) daniel@debian-dbo:~/Documents/Computing/Python_DJANGO/Django_Mosh_Hamadani/storefront-app$ 

```

- Then start again the server in the completed correct virtual environment using the correct interpreter: `python3 manage.py runserver`

## Creating Your first Project

- Every Django project is made of many apps.
- explore and inspect the `/storefront-app/storefront/settings.py` file, specially
  the `INSTALLED_APPS` list to see the default apps that come up with any new Django boiler plate project
- open a new terminal on the same project root
- **start a new app**: run `python manage.py startapp playground`. A new folder called `playground` is created next to `storefront`
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
│   └── views.py #  module to handle requests
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
    Here we can do anything backend logic:
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

-create the folder `storefront-app/playground/templates/`
-create the file: `storefront-app/playground/templates/hello.html`

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
