from rest_framework import serializers
from .models import Landlord, Tenant, Property
from django.contrib.auth.models import User






class LandlordSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ['id', 'username', 'password']
		extra_kwargs = {'password': {'write_only': True}}

	def create(self, validated_data):
		landlord = User.objects.create_user(**validated_data)
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
		extra_kwargs = {'landlord': {'required': True}}


