from django.db import models
from django.core.exceptions import ValidationError
import uuid
import datetime

# Create your models here.
def validate_date_of_birth(value):
	if value > datetime.date.today():
		raise ValidationError("Date of birth is invalid")

class Customer(models.Model):
	date_created = models.DateTimeField(auto_now_add = True)
	date_of_birth = models.DateField(validators = [validate_date_of_birth])
	email = models.EmailField()
	mobile_number = models.CharField(max_length = 10)
	name = models.CharField(max_length = 100)
	balance = models.DecimalField(default = 0,decimal_places = 5, max_digits = 30)
	account_number = models.UUIDField(default = uuid.uuid4,primary_key = True, editable = False)

	def calc_age(self):
		current = datetime.date.today()
		year_gap = current.year - self.date_of_birth.year
		if current.month < self.date_of_birth.month or (current.month == self.date_of_birth.month and current.day < self.date_of_birth.day):
		    year_gap -= 1
		return  year_gap


	# def save(self,*args, **kwargs):
	# 	self.age = self.calc_age()
	# 	super(Customer,self).save(*args, **kwargs)
	    	


