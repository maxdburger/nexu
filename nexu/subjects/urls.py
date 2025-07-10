from django.contrib import admin
from django.urls import path, include
from .views import subjects_view, subject_overview_view

urlpatterns = [
    path('subjects/', subjects_view, name='subjects'),
    path('subjects/<slug:slug>/', subject_overview_view, name='subject-overview')
]