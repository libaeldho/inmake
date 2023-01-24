
from django.urls import path

from film import views
app_name = 'film'
urlpatterns = [
    path('', views.film, name='film'),
    path('film/<int:film_id>/', views.detail, name='detail'),
    path('add/', views.add_film, name='add_film'),
    path('update/<int:id>/', views.update, name='update'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('add_new/', views.add_new, name='add_new'),

]
