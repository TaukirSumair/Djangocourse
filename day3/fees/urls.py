from django.urls import path
from fees import views

urlpatterns = [
    path('feespy/',views.feespy),
    path('feesdj/',views.feesdj),
]