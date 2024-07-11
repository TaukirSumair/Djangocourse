from django.shortcuts import render
from django.http import HttpResponse

def learn_django(request):
    return HttpResponse("Congratulations you enrolled in Django")


def learn_python(request):
    return HttpResponse("Congratulations you enrolled in Pyhton")
