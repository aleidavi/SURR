'''
	home_staff_views.py is used to create ALL 
	endpoints associated with the HOME page endpoints

	Home page represents the landing page for gov't staff:
	- will show view of ALL landlords
	- will show a view of ALL properties
	- possibly add a view of ALL tenants (who've created an account)
'''
from django.http import JsonResponse
from ..models import Landlord, Property, Tenant, TenantProperty
from ..serializers import LandlordSerializer, TenantSerializer, PropertySerializer, TenantPropertySerializer
from rest_framework.decorators import api_view
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status



@api_view(['GET'])
def home_landlord_list(request, format=None):
	"""
		Read all landlords for staff review.
	"""
	if request.method == 'GET':
		# 1. Get all the landlords (objects)
		# format returned is a list (!)
		landlords = Landlord.objects.all()
		# 2. serialize them (the landlords model obj)
		serializer = LandlordSerializer(landlords, many=True)
		#3. return json object/dict after serializing above
		return Response(serializer.data, status=status.HTTP_200_OK)
	

@api_view(['GET'])
def home_property_list(request, format=None):
	"""
		Read all properties for staff review.
	"""
	if request.method == 'GET':
		properties = Property.objects.all()
		serializer = PropertySerializer(properties, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)
	

@api_view(['GET'])
def home_tenants_list(request, format=None):
	"""
		Read all tenants for staff review.
	"""
	if request.method == 'GET':
		tenants = Landlord.objects.all()
		serializer = TenantSerializer(tenants, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)

