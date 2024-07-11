from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def projectdetail(request):

    cource = 'Pyhton'
    duration = '12 Month'
    fees = '2000'
    date=datetime.now()
    flt=5300.8888
    courcedetail={'cource':cource,'duration':duration,'fees':fees,'date':date,'ft':flt}
    student={'names':['Aman','satam','harsh']}
    return render(request,'cource.html',context=student)
