'''
	views.py is used to create ALL endpoints
'''

from django.http import JsonResponse
from .models import *
from .serializers import *
from rest_framework.decorators import api_view

from django.http import Http404
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET'])
def home_landlord_list(request, format=None):

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
	if request.method == 'GET':
		properties = Property.objects.all()

		serializer = PropertySerializer(properties, many=True)

		return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET', 'POST'])
def landlord_list(request, format=None):
	if request.method == 'POST':
		serializer = LandlordSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()

			# Used to return a response OBJ and a status value i.e. 201
			response_message = {'message': 'New Landlord profile successfully created.'}
			return Response(response_message, serializer.data, status=status.HTTP_201_CREATED)
		
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	
@api_view(['GET', 'PUT','PATCH' 'DELETE'])
def landlord_detail(request, pk, format=None):
		try:
			landlord = Landlord.objects.get(pk=pk)
		except Landlord.DoesNotExist:
			response_message = {'error message': f'This {pk} specified landlord, does not exist.'}
			return Response(response_message, status=status.HTTP_404_NOT_FOUND)
	
		if request.method == 'GET':
			serializer = LandlordSerializer(landlord)
			return Response(serializer.data, status=status.HTTP_200_OK)
	
		elif request.method == 'PUT':
			serializer = LandlordSerializer(landlord, data=request.data)
			if serializer.is_valid():
				serializer.save()
				response_message = {'message': f'Landlord {pk} profile has been updated.'}
				return Response(response_message, serializer.data, status=status.HTTP_200_OK)
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
		
		elif request.method == 'PATCH':
			serializer = LandlordSerializer(landlord)
			if serializer.is_valid():
				serializer.save()
			
			return Response(serializer.data, status=status.HTTP_200_OK)
		
		elif request.method == 'DELETE':
			landlord.delete()
			response_message = {'message': f'Landlord {pk}, data has been removed.'}
			return Response(response_message, status=status.HTTP_200_OK)

