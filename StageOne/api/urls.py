from django.urls import path
from . import views

urlpatterns = [
    path('', views.endpoint1, name='my_endpoint'),
]
