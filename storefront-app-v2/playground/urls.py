
'''
Docs:
- urlpatterns = URLConf module
- every app can have its own url app configuration
- we need to import URLConf from this app into to the main URLConf
'''

from django.urls import path
from . import views

urlpatterns = [
    path("hello/", views.say_hello),
]
