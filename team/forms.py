from django import forms
from .models import Team
from mainevent.models import User

class create_teamForm(forms.ModelForm):
	class Meta:
		model 		= Team
		fields 		= ['team_name']

class join_teamForm(forms.ModelForm):
	class Meta():
		model 		= Team
		fields 		= ['code']

class position_form(forms.ModelForm):
	# POSITION_CHOICES = ( 
	# 	("CEO", "CEO"), 
	# 	("CTO", "CTO"), 
	# 	("CFO", "CFO"), 
	# 	("CMO", "CMO"), 
	# 	("HR", "HR"),
	# )
	# position     = forms.ChoiceField(choices=POSITION_CHOICES, widget=forms.SelectMultiple, required=False)
	class Meta():
		model		= User
		fields		= ['position']

class SubmitForm(forms.ModelForm):	
	class Meta():
		model 	= Team
		fields=['presentation']