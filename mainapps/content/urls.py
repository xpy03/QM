from django.conf.urls import url, include
from django.core.paginator import Paginator
from django.shortcuts import render


from content.models import Category, Book
from content import views
urlpatterns = [
    url(r'^show/(\d+)/', views.show),
]
