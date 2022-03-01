from django import forms
from django.contrib.auth.forms import UserCreationForm
from phonenumber_field.formfields import PhoneNumberField
from django.db import transaction
from .models import User
from django.contrib.auth import get_user_model
User = get_user_model()

class UserRegistrationForm(UserCreationForm):
	# name 				= forms.CharField(max_length=60)
	name 				= forms.CharField(max_length=50)
	contact_no 			= PhoneNumberField(help_text='Add country code before the contact no.')
	email 				= forms.EmailField()
	year_of_study		= forms.IntegerField()

	class Meta(UserCreationForm.Meta):
		model 		= User
		fields 		= ['name','email','contact_no','year_of_study','roll_no','password1','password2']
	# name 				= forms.CharField(max_length=60)
	# email 				= forms.EmailField(help_text='Email Address')
	# # contact 			= PhoneNumberField(widget=forms.TextInput(attrs={'placeholder': ('')}), label=("Phone number"), required=False, help_text='Add Country Code before your contact number.')
	
	# class Meta(UserCreationForm.Meta):
	# 	model 	= User
	# 	fields 	= ['name','email','password1','password2']
class UserUpdate(forms.ModelForm):
	"""docstring for UserUpdate"""
	class Meta(object):
		"""docstring for Meta"""
		model = User
		fields = ['name', 'contact_no', 'year_of_study', 'roll_no']