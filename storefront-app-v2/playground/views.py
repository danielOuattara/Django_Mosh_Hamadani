from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def calculate():
    """Used for debugging session"""
    x = 1
    y = 2
    return x


def say_hello(request):
    """
    Here we can do anything that is backend logic:
    - CRUD from a database
    - send email
    - etc...
    """
    # return HttpResponse("Hello Django world")
    # return render(request, 'hello.html')

    # x = 1
    # y = 2

    x = calculate()
    return render(
        request,
        'hello.html',
        context={"name": "John Doe", "country": "China"}
    )
