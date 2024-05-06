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
