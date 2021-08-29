from django.contrib import admin
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

urlpatterns = [
    path('<str:room_name>/', views.index),
    path('search/lobby/', views.lobby)
]

urlpatterns += staticfiles_urlpatterns()