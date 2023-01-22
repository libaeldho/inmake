from django.urls import path
from . import views

urlpatterns = [
    path('', views.mathsoperation, name='mathsoperation'),
    path('operations/', views.clac, name='clac'),
]
