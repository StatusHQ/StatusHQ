from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse # Used to generate URLs by reversing the URL patterns

# Create your models here.
# Create your models here.
class ProfileSection(models.Model):
	def __str__(self):
		return self.section_name

	section_name = models.CharField(max_length=50)
	section_order = models.IntegerField(default=0)
	owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

class ProfileEntry(models.Model):
	def __str__(self):
		return self.entry_name

	entry = models.ForeignKey(ProfileSection, on_delete=models.CASCADE)
	entry_name = models.CharField(max_length=50)
	entry_text = models.CharField(max_length=280)
	entry_order = models.IntegerField(default=0)