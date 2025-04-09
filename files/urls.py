"""
URL configuration for files project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.contrib import admin
from django.urls import path
from .views import home_staff_views, landlord_views, property_views, tenant_views
from views.landlord_views import CreateLandlordView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('admin/', admin.site.urls),
	path('home/landlords', home_staff_views.home_landlord_list),
	path('home/properties', home_staff_views.home_property_list),
	path('home/tenants', home_staff_views.home_tenants_list),
	
	path('landlords/', landlord_views.landlord_list),
	path('landlords/<int:landlord_id>', landlord_views.landlord_detail),
	
	path('landlords/<int:landlord_id>/properties', property_views.landlord_property_list),
	path('landlords/<int:landlord_id>/properties/<property_id>', property_views.landlord_property_detail),
	
	path('tenants/', tenant_views.tenant_list),
	path('tenants/<int:tenant_id>', tenant_views.tenant_account_detail),
	path('tenants/<int:tenant_id>/properties', tenant_views.tenant_properties_detail)
]
