from django.urls import path
from . import views
urlpatterns = [

    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('home', views.home, name='home'),
    path('faculty', views.faculty, name='faculty'),
    path('contact', views.contact, name='contact'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('form', views.form, name='form'),
    path('success', views.success, name='success'),
    path('fill', views.fill, name='fill'),

]
