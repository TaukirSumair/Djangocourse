from django.shortcuts import render
from django.http import HttpResponse

def pyhtonfee(request):
    return HttpResponse(300)

def djangofee(request):
    return HttpResponse(600)
