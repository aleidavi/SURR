from rest_framework import serializers
from .models import Landlord, Tenant, Property
from django.contrib.auth.models import Landlord



class LandlordSerializer(serializers.ModelSerializer):
	class Meta:
		model = Landlord
		fields = ['id', 'username', 'password']
		extra_kwargs = {'password': {'write_only': True}}

		def create(self, validated_data):
			landlord = Landlord.objects.create_user(**validated_data)
			return landlord


class TenantSerializer(serializers.ModelSerializer):
	class Meta:
		model = Tenant
		fields = '__all__'

#
class PropertySerializer(serializers.ModelSerializer):
	class Meta:
		model = Property
		fields = '__all__'


