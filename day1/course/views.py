from django.shortcuts import render
from django.http import HttpResponse

# First Viewwwww

def learn_django(request):
    # return HttpResponse('Hello World')
    return HttpResponse('<h1>Hello World</h1>')

# Multiple View

def learn_math(request):
    a=20+20
    return HttpResponse(a)

def learn_format(request):
    a="Taukir"
    return HttpResponse(f'hello {a}')

def home(request):
    return HttpResponse('Home')