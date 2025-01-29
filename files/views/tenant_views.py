'''
	tenant_views.py is used to create ALL 
	endpoints associated with TENANT endpoints
'''
from django.http import JsonResponse
from ..models import Landlord, Property, Tenant
from ..serializers import LandlordSerializer, TenantSerializer, PropertySerializer
from rest_framework.decorators import api_view
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status


@api_view(['POST'])
def tenant_list(request, format=None):
	if request.method == 'POST':
		serializer = TenantSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()

			response_message = {'message': 'New Tenant profile successfully created.'}
			return Response(response_message, serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PATCH', 'DELETE'])
def tenant_account_detail(request, tenant_id, format=None):
	
	try:
		current_tenant = Tenant.objects.get(pk=tenant_id)
	except Tenant.DoesNotExist:
		response_message = {'error message': f'This {tenant_id} specified landlord, does not exist.'}
		return Response(response_message, status=status.HTTP_404_NOT_FOUND)
	

@api_view(['GET', 'POST', 'DELETE'])
def tenant_properties_detail(request, tenant_id, format=None):
	pass