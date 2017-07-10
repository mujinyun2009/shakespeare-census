from django import forms
from django.contrib.auth.models import User
from .models import *
from django.forms import inlineformset_factory, TextInput, formset_factory
import datetime

class TitleForm(forms.ModelForm):
	class Meta:
		model = Title
		fields = '__all__'

class SearchForm(forms.Form):
    search = forms.CharField()

class EditionForm(forms.ModelForm):
	class Meta:
		model = Edition
		exclude = ['title']

class CopyForm(forms.ModelForm):
	class Meta:
		model = Copy
		exclude = ['issue', 'created_by']

class IssueForm(forms.ModelForm):
	class Meta:
		model = Issue
		exclude = ['edition']

class ProvenanceForm(forms.ModelForm):
	class Meta:
		model = Provenance
		exclude = ['copy']

class LoginForm(forms.ModelForm):
	error_messages = {'password_mismatch': "The two password fields didn't "
					  "match. Please enter both fields again",
					  }
	password1 = forms.CharField(widget=forms.PasswordInput,
				max_length=50,
								min_length=6,
								label='Password',
								)
	password2 = forms.CharField(widget=forms.PasswordInput,
				max_length=50,
								min_length=6,
								label='Password Confirmation',
								help_text="\n Enter the same password as"
								" above, for verification.",
								)
	email = forms.CharField(max_length=75,
							required=True
							)

	class Meta:
		model = User
		fields = ['username',
				  'first_name',
				  'last_name',
				  'email',
				  'password1',
				  'password2']

# raise an error if the entered password1 and password2 are mismatched
	def clean_password2(self):
		password1 = self.cleaned_data.get("password1")
		password2 = self.cleaned_data.get("password2")
		if password1 and password2 and password1 != password2:
			raise forms.ValidationError(
				self.error_messages['password_mismatch'],
				code='password_mismatch',
			)
		return self.cleaned_data

# raise an error if email is not an upenn email or the email is already taken
	def clean_email(self):
		data = self.cleaned_data['email']
		if data.endswith("upenn.edu"):
			if User.objects.filter(email=data).exists():
				raise forms.ValidationError("This email is already used")
		else:
			raise forms.ValidationError("Must be a Penn email address")
		return data

class editProfileForm(forms.ModelForm):
	email = forms.CharField(max_length=150, required=True)
	username = forms.CharField(help_text=False)
	class Meta:
		model = User
		fields = ['username', 'first_name', 'last_name', 'email',]


	def clean_email(self):
		data = self.cleaned_data['email']
		if data.endswith("upenn.edu"):
			if not data == self.instance.email and User.objects.filter(email=data).exists():
				raise forms.ValidationError("This email is already used")
		else:
			raise forms.ValidationError("Must be a Penn email address")
		return data
