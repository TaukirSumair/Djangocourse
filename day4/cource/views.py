from django.shortcuts import render
from django.http import HttpResponse

def cource_detail(request):

    name = 'Python'
    duration = 12
    fees = 1000
    detail={'nam':name,'dur':duration,'fee':fees}
    return render(request,'courcedetail.html',detail)
