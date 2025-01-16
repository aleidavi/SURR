'''
	views.py is used to create ALL endpoints
'''

from django.http import JsonResponse
from .models import Landlord
from .serializers import LandlordSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status



@api_view(['GET', 'POST'])
def landlord_list(request):

	if request.method == 'GET':
		# 1. Get all the landlords (objects)
		# format returned is a list (!)
		landlords = Landlord.objects.all()

		# 2. serialize them (the landlords model obj)
		serializer = LandlordSerializer(landlords, many=True)

		#3. return json object/dict after serializing above
		return JsonResponse(serializer.data, safe=False)
	
	if request.method == 'POST':
		serializer = LandlordSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()

			# Used to return a response OBJ and a status value i.e. 201
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	
@api_view(['GET', 'PUT', 'DELETE'])
def landlord_detail(request, pk):
		try:
			landlord = Landlord.objects.get(pk=pk)
		except Landlord.DoesNotExist:
			return Response(status=status.HTTP_404_NOT_FOUND)
	
		if request.method == 'GET':
			serializer = LandlordSerializer(landlord)
			return Response(serializer.data)
	
		elif request.method == 'PUT':
			serializer = LandlordSerializer(landlord, data=request.data)
			if serializer.is_valid():
				serializer.save()
				return Response(serializer.data)
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
		elif request.method == 'DELETE':
			landlord.delete()
			return Response(status=status.HTTP_204_NO_CONTENT)
