from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path
from contacts import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create, name='contacts'),
    path('contacts', views.contacts, name='phonedir') 
]