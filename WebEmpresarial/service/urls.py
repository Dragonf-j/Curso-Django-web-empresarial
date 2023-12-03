from django.urls import path
from . import views

urlpatterns = [

    
    #core path

    path('', views.services, name="servicios"),

]