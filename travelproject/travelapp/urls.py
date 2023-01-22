
from django.urls import path

from travelapp import views

urlpatterns = [
    path('', views.tra, name='tra'),
    path('tour', views.tour, name="tour")

]
