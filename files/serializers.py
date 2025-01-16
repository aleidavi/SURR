from rest_framework import serializers
from .models import Landlord

class LandlordSerializer(serializers.ModelSerializer):
	class Meta:
		model = Landlord
		fields = ['id', 'first_name', 'last_name', 'business_name', 'phone_number', 'email', 'mailing_address']
		
