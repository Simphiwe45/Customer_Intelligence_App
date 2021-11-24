
from django import forms
from django.forms import ModelForm
from .models import Userprofile

class register_user(forms.ModelForm):
	class Meta:
		model=Userprofile
		fields=['Name', 'Cell_number', 'Email','Prefered_Comminication' , 'Consent']

