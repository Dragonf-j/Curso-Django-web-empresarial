from django.urls import path
from . import views

urlpatterns = [
    path('<int:pages_id>/', views.page, name="pages"),
]
