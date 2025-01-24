from rest_framework import serializers
from .models import Landlord, Tenant, Property, TenantProperty

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
#
class TenantPropertySerializer(serializers.ModelSerializer):
	class Meta:
		model = TenantProperty
		fields = '__all__'