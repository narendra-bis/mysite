from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 


class SignUpForm(UserCreationForm):
	MERRITAL_CHOICES = (
		('mr','merried'),
		('bc','bachelor')
		)
	username =forms.CharField(max_length=50, required=True, help_text='Enter Username')
	first_name = forms.CharField(max_length=50, required=False, help_text='Enter First Name')
	last_name = forms.CharField(max_length=50, required=False, help_text='Enter surname')
	email = forms.CharField(max_length=100, required=True, help_text='required valid email Id')
	birth_date = forms.DateField(help_text="YYYY/MM/DD")
	merrital_status = forms.ChoiceField(choices=MERRITAL_CHOICES)


	class Meta:
		model = User
		fields = ('username','first_name','last_name','email','birth_date','merrital_status')



