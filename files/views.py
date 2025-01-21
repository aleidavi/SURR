'''
	views.py is used to create ALL endpoints
'''

from django.http import JsonResponse
from .models import Landlord, Tenant, Property
from .serializers import LandlordSerializer
#from rest_framework import mixins
#from rest_framework import generics
from rest_framework.decorators import api_view

from django.http import Http404
#from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status



@api_view(['GET', 'POST'])
def landlord_list(request, format=None):

	if request.method == 'GET':
		# 1. Get all the landlords (objects)
		# format returned is a list (!)
		landlords = Landlord.objects.all()

		# 2. serialize them (the landlords model obj)
		serializer = LandlordSerializer(landlords, many=True)

		#3. return json object/dict after serializing above
		return Response(serializer.data, status=status.HTTP_201_CREATED, content_type=JsonResponse)
	
	if request.method == 'POST':
		serializer = LandlordSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()

			# Used to return a response OBJ and a status value i.e. 201
			return Response(serializer.data, status=status.HTTP_201_CREATED, content_type=JsonResponse)
		
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST, content_type=JsonResponse)

	
@api_view(['GET', 'PUT', 'DELETE'])
def landlord_detail(request, pk, format=None):
		try:
			landlord = Landlord.objects.get(pk=pk)
		except Landlord.DoesNotExist:
			return Response(status=status.HTTP_404_NOT_FOUND)
	
		if request.method == 'GET':
			serializer = LandlordSerializer(landlord)
			return Response(serializer.data, status=status.HTTP_201_CREATED, content_type=JsonResponse)
	
		elif request.method == 'PUT':
			serializer = LandlordSerializer(landlord, data=request.data)
			if serializer.is_valid():
				serializer.save()
				return Response(serializer.data, status=status.HTTP_201_CREATED, content_type=JsonResponse)
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST, content_type=JsonResponse)
		
		#elif request.method == 'DELETE':
			#landlord.delete()
			#return Response(status=status.HTTP_204_NO_CONTENT)



# Class-based views in DjangoRest
#class LandlordList(APIView):
	#"""
	#List of all landlords (get all), or to create a new landlord profile.
	#"""
#
	#def get(self, request, format=None):
		# 1. Get all the landlords (objects)
		# format returned is a list (!)
		#landlords = Landlord.objects.all()
#
		# 2. serialize them (the landlords model obj)
		#serializer = LandlordSerializer(landlords, many=True)
#
		#3. return json object/dict after serializing abo
		#return Response(serializer.data)
	#
	#def post(self, request, format=None):
		# 1. serialize them (the landlords model obj)
		#serializer = LandlordSerializer(data=request.data)
#
		#if serializer.is_valid():
			#serializer.save()
			#return Response(serializer.data, status=status.HTTP_201_CREATED)
#
		#return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	#
#
#class LandlordDetail(APIView):
	#"""
	#Retrieve update, or delete a snippet instance.
	#"""
#
	#def get_object(self, pk):
		#"""
		#- helper function to get object 
		#- uses error handling
		#- pk refers to PRIMARY KEY
		#"""
		#try:
			#return Landlord.obects.get(pk=pk)
		#
		#except Landlord.DoesNotExist:
			#raise Http404
#
	#def get(self, request, pk, format=None):
		#landlord = self.get_object(pk)
		#serializer = LandlordSerializer(landlord)
		#return Response(serializer.data)
	#
	#def put(self, request, pk, format=None):
		#landlord = self.get_object(pk=pk)
		#serializer = LandlordSerializer(landlord, data=request.data)
		#if serializer.is_valid():
			#serializer.save()
			#return Response(serializer.data)
		#
		#return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	#
	#def delete(self, request, pk, format=None):
		#landlord = self.get_object(pk)
		#landlord.delete()
		#return Response(status=status.HTTP_204_NO_CONTENT)
