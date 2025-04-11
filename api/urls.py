from django.urls import path, include
from ..files import views


url_patterns = [
    path('properties/', views.PropertiesListCreate.as_view(), name='property-list'),
    path('properties/delete/<int:pk>/', views.PropertyDelete.as_view(), name='delete-property'),
]