from django.urls import path
from . import views

app_name ='calculate'
urlpatterns = [
    path('', views.calculate, name='calculate'),
]