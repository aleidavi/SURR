'''
	tenant_views.py is used to create ALL 
	endpoints associated with TENANT endpoints
'''
from django.http import JsonResponse
from ..models import Landlord, Property, Tenant, TenantProperty
from ..serializers import LandlordSerializer, TenantSerializer, PropertySerializer, TenantPropertySerializer
from rest_framework.decorators import api_view
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status


