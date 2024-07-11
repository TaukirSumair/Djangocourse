from . import views
from django.urls import path

urlpatterns = [
    path('djfee',views.djangofee),
    path('pyfee',views.pyhtonfee)
]
