from django.urls import path
from enroll import views  

urlpatterns = [
    path('fill/',views.getData),
]
