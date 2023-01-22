
from django.urls import path

from vegapp import views

urlpatterns = [
    path('', views.veg, name='veg')
]
