
from django.db import models
from django.core.validators import RegexValidator


class Landlord(models.Model):
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	busines_name = models.CharField(max_length=200)
	phone_number = models.CharField(max_length=15, validators=[
        RegexValidator(r'^\+?1?\d{9,15}$', message="Phone number must be entered in this format: '+[Country Code][Number]'. Up to 15 digits allowed.")
    ])

	email = models.CharField()
	mailing_address = models.CharField()

	# dunder init method to have this object return
	# the object's Landlord Profile Name
	def __str__(self):
		return self.first_name + ' ' + self.last_name
