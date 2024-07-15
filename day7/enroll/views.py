from django.shortcuts import render
from .forms import StudentRegistration

def getData(request):
    sr=StudentRegistration(auto_id='taukir_%s',label_suffix='-')
    sr.order_fields(field_order=['email','name']) #shuffling Field
    return render(request,'enroll/enrollform.html',{'form':sr})

