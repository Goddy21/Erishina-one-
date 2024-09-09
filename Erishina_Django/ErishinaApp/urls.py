from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('goals', views.goals, name='goals'),
    path('projects', views.projects, name='projects'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout')
]
