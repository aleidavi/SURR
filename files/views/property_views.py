'''
	property_views.py is used to create ALL 
	endpoints associated with PROPERTY endpoints
'''
from django.http import JsonResponse
from files.models import Landlord, Property, Tenant
from files.serializers import LandlordSerializer, PropertySerializer
from rest_framework.decorators import api_view
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404


@api_view(['GET', 'POST', 'DELETE']) 
def landlord_property_list(request, landlord_id, format=None):
	"""
		Endpoint route allows landlord user to:
			read all properties, of the current landlord,
			post new properties (add/create) to their current properties list,
			and delete a property from the properties list belonging to the landlord.
	"""
	try:
		#print('Checking prior to landlord ID')
		landlord = Landlord.objects.get(pk=landlord_id)
		#print(f'Landlord of id {landlord_id}')
	except Landlord.DoesNotExist:
		response_message = {'message': f'Landlord {landlord_id} not found.'}
		return Response(response_message, status=status.HTTP_404_NOT_FOUND)
	

	# GET All properties of landlord_id
	landlord_property_list = landlord.properties.all()
	if request.method == 'GET':
		serializer = PropertySerializer(landlord_property_list, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)
	
	# POST new property to landlord_id
	elif request.method == 'POST':
		
		updated_data = request.data
		updated_data['landlord'] = landlord_id
		serializer = PropertySerializer(data=updated_data)
		if serializer.is_valid():
			serializer.save()

			# Used to return a response OBJ and a status value i.e. 201
			return Response(serializer.data, status=status.HTTP_201_CREATED)

		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	# DELETE a property from landlord_id properties
	elif request.method == 'DELETE':
		current_property_id = request.data.get('id', None)
		
		if current_property_id is None:
			return Response({'error': 'Property selected for deletion is invalid.'}, status=status.HTTP_400_BAD_REQUEST)

		
		property_instance = get_object_or_404(Property, pk=current_property_id, landlord=landlord)
		property_instance.delete()
		
		response_message = {'message': f'Property {current_property_id}, data has been removed from Landlord {landlord_id}.'}
		return Response(response_message, status=status.HTTP_200_OK)


@api_view(['GET', 'PATCH'])
def landlord_property_detail(request, landlord_id, property_id, format=None):
	"""
	 GET /landlords/landlord_id/properties/<property_id> -> 
	 	Get the current property of property_id, for landlord_id specified
		 
	 PATCH /landlords/landlord_id/properties/<property_id> ->
	 	Update the current property of property_id for landlord_id specified

	"""


	try:
		current_property = Property.objects.get(pk=property_id)
	except Property.DoesNotExist:
		response_message = {'message': f'Property {property_id} not found.'}
		return Response(response_message, status=status.HTTP_404_NOT_FOUND)

	if request.method == 'GET':
		serializer = PropertySerializer(current_property)
		return Response(serializer.data, status=status.HTTP_200_OK)


	elif request.method == 'PATCH':
		serializer = PropertySerializer(current_property, data=request.data, partial=True)
		if serializer.is_valid():
			serializer.save()
		response_message={'message': f'Property {property_id} information successfully updated.'}
		return Response(serializer.data, status=status.HTTP_200_OK)



	