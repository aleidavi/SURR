'''
	landlord_views.py is used to create ALL 
	endpoints associated with landlord endpoints

'''
from django.http import JsonResponse
from ..models import Landlord, Property, Tenant, TenantProperty
from ..serializers import LandlordSerializer, PropertySerializer
from rest_framework.decorators import api_view
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status

@api_view(['POST'])
def landlord_list(request, format=None):
	if request.method == 'POST':
		serializer = LandlordSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			# Used to return a response OBJ and a status value i.e. 201
			response_message = {'message': 'New Landlord profile successfully created.'}
			return Response(response_message, serializer.data, status=status.HTTP_201_CREATED)
		
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	

@api_view(['GET','PATCH' 'DELETE'])
def landlord_detail(request, pk, format=None):
		try:
			landlord = Landlord.objects.get(pk=pk)
		except Landlord.DoesNotExist:
			response_message = {'error message': f'This {pk} specified landlord, does not exist.'}
			return Response(response_message, status=status.HTTP_404_NOT_FOUND)
	
		if request.method == 'GET':
			serializer = LandlordSerializer(landlord)
			return Response(serializer.data, status=status.HTTP_200_OK)	
		elif request.method == 'PATCH':
			serializer = LandlordSerializer(landlord, data=request.data,partial=True)
			if serializer.is_valid():
				serializer.save()
			
			return Response(serializer.data, status=status.HTTP_200_OK)
		
		elif request.method == 'DELETE':
			landlord.delete()
			response_message = {'message': f'Landlord {pk}, data has been removed.'}
			return Response(response_message, status=status.HTTP_200_OK)

