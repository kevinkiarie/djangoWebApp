from django import forms
from models import CustomUser, postmodel, UserProf
from django.utils import timezone
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class UpdateProfile(forms.ModelForm):
	username = forms.CharField(required = False)
	email = forms.EmailField(required=True)
	first_name =  forms.CharField(required = False)
	last_name = forms.CharField(required = False)
	

class UserForm(forms.ModelForm):
	#password_comfirm = forms.
	class Meta:
		model = CustomUser
		fields = ('username','email','password', 'telephone', 'picture')

	def __init__(self, *args, **kwargs):
		super(UserForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_id = "user_form"
		self.helper.form_role = "form"
		self.helper.from_class = "form-inline"
		self.helper.from_method = "post"
		self.helper.help_text_inline = True
		self.helper.form_action = "/main/register/"
		self.helper.add_input(Submit("Submit", "Submit"))
		



class UserProfForm(forms.ModelForm):
	class Meta:
		model = UserProf
		fields = ( "Register_as", "town","offices")
	def __init__(self, *args, **kwargs):
		super(UserProfForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_id = "user_form"
		self.helper.from_class = "form-inline"
		self.helper.from_method = "post"
		self.helper.form_action = "/main/fin_register/"
		self.helper.add_input(Submit("Submit", "Submit"))
		


class postmodelform(forms.ModelForm):
	class Meta:
		model = postmodel
		fields = ("property_type", "name","room", "price", "property_location", "area",  "property_description","property_picture")

	def __init__(self, *args, **kwargs):
		super(postmodelform, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_id = "post_form"
		self.helper.from_class = "form-inline"
		self.helper.from_method = "post"
		self.helper.form_action = "/main/add_todo/"
		self.helper.add_input(Submit("Submit", "Submit"))









class CustomUserCreationForm(UserCreationForm):
	"""A form that creates a user, with no privileges, from the given email and password."""
	def __init__(self, *args, **kargs):
		super(CustomUserCreationForm, self).__init__(*args, **kargs)
		del self.fields['username']
	class Meta:
		model = CustomUser
		fields = ("email",)

class CustomUserChangeForm(UserChangeForm):
	"""A form for updating users. Includes all the fields on the user, but replaces the password field with admin's password hash display 		field."""
	def __init__(self, *args, **kargs):
		super(CustomUserChangeForm, self).__init__(*args, **kargs)
		del self.fields['username']

	class Meta:
		model = CustomUser
		exclude = []
