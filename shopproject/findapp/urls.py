from django.urls import path

from  . import views

app_name = 'findapp'

urlpatterns = [
    path('', views.SearchResult, name='SearchResult'),
]
