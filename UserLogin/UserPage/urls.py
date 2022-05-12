from django import views
from django.urls import path,include
from .import views

urlpatterns = [
    path('home',views.home),
    path('page',views.page),
    path('logout',views.logout)
]