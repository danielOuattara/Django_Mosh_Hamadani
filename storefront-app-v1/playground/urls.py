from django.urls import path
from . import views

'''
 urlpatterns = URLConf module
 - every app can it own url app configuration
 - we need to import this URLConf to the main URLConf
'''
urlpatterns = [
    path("hello/", views.say_hello)
]
