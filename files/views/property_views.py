'''
	property_views.py is used to create ALL 
	endpoints associated with PROPERTY endpoints
'''
from django.http import JsonResponse
from ..models import Landlord, Property, Tenant, TenantProperty
from ..serializers import LandlordSerializer, TenantSerializer, PropertySerializer, TenantPropertySerializer
from rest_framework.decorators import api_view
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404


@api_view(['GET', 'POST', 'DELETE'])
def landlord_property_list(request, pk, format=None):
	"""
		Endpoint route allows landlord user to:
			read all properties, of the current landlord,
			post new properties (add/create) to their current properties list,
			and delete a property from the properties list belonging to the landlord.
	"""
	try:
		landlord = Landlord.objects.get(pk=pk)
	except Landlord.DoesNotExist:
		response_message = {'message': f'Landlord {pk} not found.'}
		return Response(response_message, status=status.HTTP_404_NOT_FOUND)
	
	landlord_property_id_list = landlord.properties
	if request.method == 'GET':
		properties_list = Property.objects.all().filter(id__in=landlord_property_id_list)
		serializer = PropertySerializer(properties_list)

		return Response(serializer.data, status=status.HTTP_200_OK)
	
	
	elif request.method == 'POST':
		new_property_id = request.data.get('id', None)
		if new_property_id == None:
			return Response({'error': 'Property ID required. New property cannot be added without it\'s property_id'},
				   status=status.HTTP_400_BAD_REQUEST)
		
		landlord.properties.append(new_property_id)
		landlord.save()

		serializer = LandlordSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()

			# Used to return a response OBJ and a status value i.e. 201
			response_message = {'message': 'New property posted to Landlord {pk} list successfully created.'}
			return Response(response_message, serializer.data, status=status.HTTP_201_CREATED)

		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	elif request.method == 'DELETE':
		current_property_id = request.data.get('id', None)
		
		if current_property_id is None:
			return Response({'error': 'Property ID is required.'}, status=status.HTTP_400_BAD_REQUEST)

		elif current_property_id in landlord.properties:
			index = landlord.properties.find(current_property_id)
			landlord.properties.pop(index)
			landlord.save()

			property_instance = get_object_or_404(Property, pk=current_property_id)
			property_instance.delete()
		
			response_message = {'message': f'Property {current_property_id}, data has been removed from {pk}.'}
			return Response(response_message, status=status.HTTP_200_OK)
		else:
			return Response({'error': 'Property ID not found in landlord\'s properties.'}, status=status.HTTP_400_BAD_REQUEST)

@api_view([])
def landlord_property_detail(request, pk, format=None):
	"""
	 GET /landlords/<landlord_id>/properties/<property_id> -> 
	 PATCH /landlords/<landlord_id>/properties/<property_id>  ->
	"""	
	