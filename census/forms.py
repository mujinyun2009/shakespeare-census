from django import forms
from django.contrib.auth.models import User
from .models import *
from django.forms import inlineformset_factory, TextInput, formset_factory
import datetime

class TitleForm(forms.ModelForm):
	title=forms.CharField(required=True)
	class Meta:
		model = Title
		fields = '__all__'

class SearchForm(forms.Form):
    search = forms.CharField()

class EditionForm(forms.ModelForm):
	Edition_format=forms.CharField(required=False)
	class Meta:
		model = Edition
		exclude = ['title']

class CopyForm(forms.ModelForm):
	Owner=forms.CharField(required=True)
	thumbnail_URL = forms.URLField(widget=forms.TextInput(attrs={'size':'80'}), error_messages={'invalid': 'Enter a valid url.'}, required=False)
	NSC=forms.IntegerField(label="NSC", initial=0, required=False)
	Shelfmark=forms.CharField(required=False)
	Height=forms.IntegerField(initial=0, required=False)
	Width=forms.IntegerField(initial=0, required=False)
	Marginalia=forms.CharField(required=False)
	Condition=forms.CharField(required=False)
	Binding=forms.CharField(required=False)
	Binder=forms.CharField(required=False)
	Bookplate=forms.CharField(required=False)
	Bookplate_Location=forms.CharField(required=False)
	Bartlett1939=forms.IntegerField(initial=0, required=False)
	Bartlett1939_Notes=forms.CharField(required=False)
	Bartlett1916=forms.IntegerField(initial=0, required=False)
	Bartlett1916_Notes=forms.CharField(required=False)
	Lee_Notes=forms.CharField(required=False)
	Library_Notes=forms.CharField(required=False)
	copynote=forms.CharField(required=False)
	prov_info=forms.CharField(widget=forms.Textarea, required=False)

	class Meta:
		model = Copy
		exclude = ['issue', 'created_by']

	def clean_url(self):
		entered_URL=self.cleaned_data['thumbnail_URL']
		if entered_URL and not entered_URL.startswith('http://'):
			entered_URL='http://'+entered_URL
			cleaned_data['thumbnail_URL']=entered_URL
		return cleaned_data

class IssueForm(forms.ModelForm):
	error_messages={"Incorrect year format": "Invalid published year. Please follow the examples to enter correct information."}

	DEEP=forms.IntegerField(required=False, initial=0)
	year=forms.CharField(label="Year published", help_text="Examples: 1600, 1600?, 1650-1700, 1650-1700?",required=True)
	notes=forms.CharField(label="Notes about the issue", required=False)
	Variant_Description=forms.CharField(required=False)
	class Meta:
		model = Issue
		exclude = ['edition', 'start_date', 'end_date']

	def clean_year(self):
		entered_year=self.cleaned_data['year']
		length = len(entered_year)
		if entered_year.endswith('?'):
			entered_year=entered_year[:length-1]
		hyphen = entered_year.find('-')
		if hyphen > -1:
			if hyphen==0 or hyphen == length - 1:
				raise forms.ValidationError(self.error_messages['Incorrect year format'])
			else:
				start_date=entered_year[:hyphen]
				end_date=entered_year[hyphen+1:]
				if not start_date.isdigit() or not end_date.isdigit():
					raise forms.ValidationError(self.error_messages['Incorrect year format'])
		else:
			if not entered_year.isdigit():
				raise forms.ValidationError(self.error_messages['Incorrect year format'])
		return entered_year


class ProvenanceForm(forms.ModelForm):
	class Meta:
		model = Provenance
		exclude = ['copy']

class LoginForm(forms.ModelForm):
	error_messages = {'password_mismatch': "The two password fields didn't "
					  "match. Please enter both fields again.",
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
				raise forms.ValidationError("This email is already used.")
		else:
			raise forms.ValidationError("Must be a Penn email address.")
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
				raise forms.ValidationError("This email is already used.")
		else:
			raise forms.ValidationError("Must be a Penn email address.")
		return data
