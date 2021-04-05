from django.urls import path, include
from . import views

urlpatterns = [
    path('about/', views.about, name= 'about'),
    path('', views.home, name='home'),
    path('teams/', views.team, name ='team'),
    path('news/', views.news, name ='news'),
    path('contact/', views.contact, name ='contact'),
    path('appointment/', views.appointment, name = 'appointment'),
    path('join/', views.join, name = 'add-doctor'),
    path('register/', views.register_request, name = 'register'),
    path('logout/', views.logout_request, name = 'logout'),
    path('login/', views.login_request, name = 'login'),
]