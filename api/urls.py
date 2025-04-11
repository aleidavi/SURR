from django.urls import path
from files.views import property_views


urlpatterns = [
    path('properties/', property_views.PropertyListCreate.as_view(), name='property-list'),
    path('properties/delete/<int:pk>/', property_views.PropertyDelete.as_view(), name='delete-property'),
]