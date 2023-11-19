from django.urls import path
from . import views

urlpatterns = [

    
    #core path
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('services/', views.services, name="servicios"),
    path('store/', views.store, name="tienda"),
    path('contac/', views.contact, name="contacto"),
    path('blog/', views.blog, name="blog"),
    path('sample/', views.sample, name="ejemplo"),
]
