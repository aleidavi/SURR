'''
	views.py is used to create ALL endpoints
'''

from django.http import JsonResponse
from .models import Landlord
from .serializers import LandlordSerializer

#def index(request):
#	return HttpResponse('Hello World')

def landlord_list(request):
	# 1. Get all the landlords (objects)
	# format returned is a list (!)
	landlords = Landlord.objects.all()

	# 2. serialize them (the landlords model obj)
	serializer = LandlordSerializer(landlords, many=True)

	#3. return json object/dict after serializing above
	return JsonResponse(serializer.data, safe=False)