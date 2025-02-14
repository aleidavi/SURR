from rest_framework import serializers
from .models import Landlord, Tenant, Property

from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = Landlord
		field = ['id', 'username', 'password']
		extra_kwargs = {'password': {
			'write_only': True
		}}

		def create(self, validated_data):
			landlord = Landlord.objects.create_user(**validated_data)
			return landlord


class LandlordSerializer(serializers.ModelSerializer):
	class Meta:
		model = Landlord

		fields = '__all__'


class TenantSerializer(serializers.ModelSerializer):
	class Meta:
		model = Tenant
		fields = '__all__'

#
class PropertySerializer(serializers.ModelSerializer):
	class Meta:
		model = Property
		fields = '__all__'




