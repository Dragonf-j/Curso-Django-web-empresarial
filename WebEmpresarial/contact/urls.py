from django.urls import path
from . import views

urlpatterns = [
    #contact path
    path('', views.contact, name="contacto"),

]
