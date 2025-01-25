
from django.db import models
from django.core.validators import RegexValidator
from django.contrib.postgres.fields import ArrayField


class Landlord(models.Model):
	
	username = models.CharField(max_length=500)
	password = models.CharField(max_length=50)
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	business_name = models.CharField(max_length=200, blank=True, null=True, default=None)
	phone_number = models.CharField(max_length=15, validators=[
        RegexValidator(r'^\+?1?\d{9,15}$', message="Phone number must be entered in this format: '+[Country Code(International)][Number]'. Up to 15 digits allowed.")
    ])

	email = models.CharField(max_length=200)
	mailing_address = models.CharField(max_length=200)
	properties = ArrayField(models.IntegerField(), blank=True, default=list)

	# dunder init method to have this object return
	# the object's Landlord Profile
	# Name
	def __str__(self):
		return f"{self.first_name} {self.last_name}"
	
	# Meta class used inside of landlord simply to format data
	# when Landlord model is called upon
	# Landlord instance data will be ordered based on first_name
	class Meta:
		ordering = ['first_name']

class Tenant(models.Model):
	username = models.CharField(max_length=500)
	password = models.CharField(max_length=50)
	current_address = models.CharField(max_length=500)
	phone_number = models.CharField(max_length=15, validators=[
		RegexValidator(r'^\+?1?\d{9,15}$', message="Phone number must be entered in this format: '+[Country Code][Number]'. Up to 15 digits allowed.")
	])
	email = models.CharField(max_length=200)
	monthly_rent = models.PositiveBigIntegerField()
	properties = ArrayField(models.IntegerField(), blank=True, default=list)
	landlord = models.ForeignKey(Landlord, on_delete=models.CASCADE)


class Property(models.Model):

	address = models.CharField(max_length=300)
	unit_quantity = models.PositiveIntegerField()
	property_type = models.CharField(max_length=200)
	monthly_rent = models.PositiveBigIntegerField()
	last_increase_date = models.DateField(null=True, blank=True, default=None)
	rent_increase_percentage = models.IntegerField(null=True, blank=True, default=None)
	ocupancy_start_date = models.DateField(null=True, blank=True, default=None)
	ocupancy_status = models.CharField(max_length=25)
	landlord = models.ForeignKey(Landlord, on_delete=models.CASCADE)
	tenants = ArrayField(models.IntegerField(), blank=True, default=list)

class TenantProperty(models.Model):
	tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
	property = models.ForeignKey(Property, on_delete=models.CASCADE)