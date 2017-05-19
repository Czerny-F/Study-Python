from django.shortcuts import render  # noqa

# Create your views here.
from django.http import HttpResponse


def index(request, param='no params'):
    print(param)
    print(request)

    return HttpResponse("Hello, world. You're at the polls index.")


def test_method(request):
    return HttpResponse("Test method called")
    # pass
