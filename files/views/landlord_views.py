'''
	landlord_views.py is used to create ALL 
	endpoints associated with landlord endpoints

'''
from django.http import JsonResponse
from ..models import Landlord, Property, Tenant
from ..serializers import LandlordSerializer, PropertySerializer
from rest_framework.decorators import api_view
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def landlord_list(request, format=None):

	landlords_list = Landlord.objects.all()

	if request.method == 'GET':
		serializer = LandlordSerializer(landlords_list, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)

	if request.method == 'POST':
		new_username = request.data.get('username', None)
		if new_username == None:
			return Response({'error': 'Username is required.'}, status=status.HTTP_400_BAD_REQUEST)
		
		if Landlord.objects.filter(username=new_username).exists():
			return Response({'error': 'The username entered is not available. Please choose a different username.'}, status=status.HTTP_400_BAD_REQUEST)

		serializer = LandlordSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()

			# TO - DO -> Remove response message
			# Used to return a response OBJ and a status value i.e. 201
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	

@api_view(['GET','PATCH', 'DELETE'])
def landlord_detail(request, landlord_id, format=None):
		try:
			landlord = Landlord.objects.get(pk=landlord_id)
		except Landlord.DoesNotExist:
			response_message = {'error message': f'This specified landlord {landlord_id}, does not exist.'}
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
			response_message = {'message': f'Landlord {landlord_id}, data has been removed.'}
			return Response(response_message, status=status.HTTP_200_OK)