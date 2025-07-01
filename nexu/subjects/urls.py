from django.contrib import admin
from django.urls import path, include
from .views import subjects_view

urlpatterns = [
    path('subjects/', subjects_view),
]