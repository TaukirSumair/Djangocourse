from django.shortcuts import render
from .models import Student

def getdata(request):
    data=Student.objects.all()
    print(data)
    return render(request,'enroll/data.html',{'data':data})
