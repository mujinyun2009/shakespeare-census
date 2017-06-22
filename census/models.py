from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm
#from pillow import Image
#Create your models here.
class Title(models.Model):
	title = models.CharField(max_length=128, unique=False)
	Apocryphal = models.BooleanField(default=False)
	def __unicode__(self):
		return self.title

class Edition (models.Model):
	title = models.ForeignKey(Title)
	year = models.IntegerField(default=0)
	Edition_number = models.IntegerField(default=0)
	Edition_format = models.CharField(max_length=10)
	def __str__(self):
		return "%s Edition %s" % (self.title, self.Edition_number)
class Issue (models.Model):
	edition = models.ForeignKey(Edition, unique=False)
	STC_Wing = models.IntegerField(default=0)
	DEEP = models.IntegerField(default=0)
	ESTC = models.IntegerField(default=0)
	Variant_Description = models.CharField(max_length=1000)
	def __str__(self):
		return "%s Issue %s" % (self.edition, self.STC_Wing)
class Copy (models.Model):
	issue = models.ForeignKey(Issue, unique=False)
	thumbnail_URL = models.URLField(max_length=200)
	NSC = models.IntegerField(default=0)
	Owner = models.CharField(max_length=40)
	Shelfmark = models.IntegerField(default=0)
	Height = models.IntegerField(default=0)
	Width = models.IntegerField(default=0)
	Marginalia = models.CharField(max_length=100, null=True)
	Condition = models.CharField(max_length=200)
	Binding = models.CharField(max_length=200)
	Binder = models.CharField(max_length=40)
	Bookplate = models.CharField(max_length=40)
	Bookplate_Location = models.CharField(max_length=100)
	Barlett1939 = models.IntegerField(default=0)
	Barlet1939_Notes = models.CharField(max_length=1000)
	Barlet1916 = models.IntegerField(default=0)
	Barlet1916_Notes = models.CharField(max_length=1000)
	Lee_Notes = models.CharField(max_length=2000)
	Library_Notes=models.CharField(max_length=2000)
	def __str__(self):
		return  "%s %s" % (self.issue, self.NSC)
	class Meta:
		verbose_name_plural = "copies"

class Provenance (models.Model):
	copy = models.ForeignKey(Copy, on_delete=models.CASCADE)
	name = models.CharField(max_length=40)
	bio = models.CharField(max_length=1000)
	def __str__(self):
		return "%s %s" % (self.copy, self.name)
class BookPlate (models.Model):
	copy = models.ForeignKey(Copy, on_delete=models.CASCADE)
	text = models.CharField(max_length=100)
	def __str__(self):
		return  "%s" % (self.text)
class BookPlate_Location (models.Model):
	copy = models.ForeignKey(Copy, on_delete=models.CASCADE)
	Location = models.CharField(max_length=100)
	def __str__(self):
		return  "%s" % (self.Location)
class Transfer(models.Model):
	copy = models.ForeignKey(Copy, on_delete=models.CASCADE)
	bleh = models.CharField(max_length=100)
	def __str__(self):
		return  "%s" % (self.bleh)
class Transfer_Value (models.Model):
	copy = models.ForeignKey(Copy, on_delete=models.CASCADE)
	Value = models.CharField(max_length=100)
	def __str__(self):
		return  "%s" % (self.Value)

class UserProfile(models.Model):
	user = models.OneToOneField(User)
	def __unicode__(self):
		return self.user.username
	def delete(self, *args, **kwargs):
		self.user.delete()
		return super(UserProfile,self).delete(*args, **kwargs)

class Entity(models.Model):
	name = models.CharField(max_length=200)
	notes = models.CharField(max_length=500)
	def __str__(self):
		return "%s" % (self.name)
	class Meta:
		verbose_name_plural = "entities"

class Transaction(models.Model):
	copy = models.ForeignKey(Copy, on_delete=models.CASCADE)
	buyer = models.ForeignKey(Entity, related_name="entity_buyer", max_length=100)
	seller = models.ForeignKey(Entity, related_name="entity_seller", max_length=100)
	# data_transaction = models.CharField(max_length=200)
	date = models.DateField()
	price = models.DecimalField(max_digits = 10, decimal_places=2)
	def __str__(self):
		return "Sold from %s to %s" % (self.seller, self.buyer)
