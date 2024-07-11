from course import views
from django.urls import path

urlpatterns = [
    path('django/',views.learn_django),
    path('python/',views.learn_python),
]
