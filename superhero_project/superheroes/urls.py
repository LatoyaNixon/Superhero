from django.conf.urls import url
from django.urls import path
from django.urls.resolvers import URLPattern

from .import views

app_name = 'superheroes'
urlpatterns = [
    path('', views.index, name='index')
]