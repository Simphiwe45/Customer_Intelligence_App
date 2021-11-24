from django.db import models
from django import forms
from django.utils.timezone import now
# Create your models here.
class Userprofile(models.Model):
	Name = models.CharField(blank= False ,max_length=20)
	Cell_number = models.CharField(blank=False,  max_length=20)
	Email=models.EmailField(max_length=254)
	Prefered_Comminication=models.CharField( max_length=6,default= "Phone", choices=[('P',"Phone"),('E',"Email")])
	Consent = models.BooleanField(default= False)
	Entry_counter = models.IntegerField(default= 1)
	created_date = models.DateTimeField(default=now, editable=False)

	def __str__(self):
		return f'{self.Name}'

