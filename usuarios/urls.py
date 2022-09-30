from django.urls import path
from . import views

urlpatterns = [
    path('cadastro', views.cadastro, name='cadastro'),
    path('login', views.login, name='login' ),
    path('dashboard', views.dash, name='dashboard'),
    path('logout', views.logout, name='logout'),
]