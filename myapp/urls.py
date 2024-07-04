from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.hola),
    path('categoria/', views.categoria),
    path('login/', views.login),
    
]