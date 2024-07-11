from django.shortcuts import render
from django.http import HttpResponse

def feespy(request):
    return render(request,"courcefees.html")
def feesdj(request):
    return HttpResponse(100)