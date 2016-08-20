
from django.db import models
from django.utils import timezone
from django.utils.http import urlquote
from django.utils.translation import ugettext_lazy as _
from django.core.mail import send_mail
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.models import BaseUserManager




class CustomUserManager(BaseUserManager):
	def _create_user(self, email, password,is_staff, is_superuser, **extra_fields):
		"""Creates and saves a User with the given email and password. """
		now = timezone.now()
		if not email:
			raise ValueError('The given email must be set')
		email = self.normalize_email(email)
		user = self.model(email=email, is_staff=is_staff, is_active=True, is_superuser=is_superuser, last_login=now, date_joined=now, **extra_fields)
		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_user(self, email, password=None, **extra_fields):
		return self._create_user(email, password, False, False, **extra_fields)
	def create_superuser(self, email, password, **extra_fields):
		return self._create_user(email, password, True, True, **extra_fields)



# Create your models here.
class CustomUser(AbstractBaseUser, PermissionsMixin):
	email = models.EmailField(_('email address'), max_length=254, unique=True)
	username = models.CharField(_('username'), max_length=30)
	first_name = models.CharField(_('first name'), max_length=30, blank=True)
	last_name = models.CharField(_('last name'), max_length=30, blank=True)
	telephone = models.CharField(_('phone number'), max_length=15)
	is_staff = models.BooleanField(_('staff status'), default=False, help_text=_('Designates whether the user can log into this admin ' 'site.'))
	is_active = models.BooleanField(_('active'), default=True,help_text=_('Designates whether this user should be treated as ''active. Unselect this instead of deleting accounts.'))
	date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
	picture = models.ImageField(_("profile picture"), upload_to="images/users/%Y/%m/%d/", default="images/1.jpg",blank=True)
	


	objects = CustomUserManager()
	
	USERNAME_FIELD = 'email'

	REQUIRED_FIELDS = []


	class Meta:
		verbose_name = _('user')
		verbose_name_plural = _('users')

	def get_absolute_url(self):
		return "/users/%s/" % urlquote(self.email)

	def get_full_name(self):
		"""Returns the first_name plus the last_name, with a space in between."""
		full_name = '%s %s' % (self.first_name, self.last_name)
		return full_name.strip()

	
	def get_short_name(self):
		"Returns the short name for the user."
		return self.first_name

	
	def email_user(self, subject, message, from_email=None):
		"""Sends an email to this User. """
		send_mail(subject, message, from_email, [self.email])







class UserProf(models.Model):
	OWNER = "OWNER"
	TENANT = "TENANT"
	AGENT = "AGENT"
	USER_CHOICES = (
		(OWNER, "Owner"),
		(AGENT, "Agent"),
		(TENANT, "Tenant"),
	)
	user = models.ForeignKey(CustomUser)
	created_at = models.DateTimeField(auto_now=True)
	Register_as = models.CharField(max_length=6, choices=USER_CHOICES, default=TENANT, help_text="Users have different permissions")
	town = models.CharField(max_length=30, help_text="Your business' town")
	offices = models.CharField(max_length=30, help_text="The building your offices are located", blank=True)
	

	def __unicode__(self):
		return self.user


class postmodel(models.Model):
	BEDSITTER = "BEDSITTER"
	SINGLE = "SINGLE"
	DOUBLE = "DOUBLE"
	SHOP = "SHOP"
	SELF_CONTAINED = "SELF_CONTAINED"
	WAREHOUSE = "WAREHOUSE"
	OFFICE = "OFFICE"
	FACTORY = "FACTORY"
	COMMERCIAL_KITCHEN = "COMMERCIAL_KITCHEN"
	CLUB = "CLUB"
	TYPE_CHOICES = (
		(BEDSITTER, "Bedsitter"),
		(SINGLE, "Single"),
		(DOUBLE, "Double"),
		(SELF_CONTAINED, "Self_contained"),
		(SHOP, "Shop"),
		(OFFICE, "Offices"),
		(WAREHOUSE, "Warehouse"),
		(FACTORY, "Factory"),
		(COMMERCIAL_KITCHEN, "Commercial Kitchen"),
		(CLUB, "Club"),
		)
	owner = models.ForeignKey(CustomUser)
	name = models.CharField(max_length=30, help_text="e.g name of the building")
	created_at = models.DateTimeField(auto_now=True)
	price = models.IntegerField()
	property_type = models.CharField(max_length=15, choices=TYPE_CHOICES, default=BEDSITTER)
	property_picture = models.ImageField(upload_to="/media/images/property/%Y/%m/%d/",default="/media/images/1.jpg", blank=True)
	property_location = models.CharField(max_length=50, help_text="Town where property is")
	area = models.CharField(max_length=25, help_text="Neighbourhood name/Jina ya Mtaa")
	room = models.IntegerField(help_text="room/ door number")
	property_description = models.CharField(max_length=140, help_text="Describe the property", blank=True)
	

	def __unicode__(self):
		return self.name
		
	
	
