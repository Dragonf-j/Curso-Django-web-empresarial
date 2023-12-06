from django.urls import path
from . import views

urlpatterns = [

    
    #core path
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('store/', views.store, name="tienda"),
    path('contac/', views.contact, name="contacto"),
    path('sample/', views.sample, name="ejemplo"),
]
