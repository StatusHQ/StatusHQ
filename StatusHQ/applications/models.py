from django.db import models
from django.urls import reverse # Used to generate URLs by reversing the URL patterns
from django.contrib.auth.models import User

#class CurrentApplications(models.Model):
'''Model represting all current applications.'''

# Create your models here.
class Application(models.Model):
	''' Model representing instance of an application'''
	company = models.CharField(max_length = 50)
	position = models.CharField(max_length = 50)
	date_applied = models.DateField(null=True, blank=True)
	deadline = models.DateField(null=True, blank=True)
	owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

	APP_STATUS = (
		('p', 'In Progress'),
		('a', 'Applied'),
		('i', 'Interviewing'),
		('o', 'Offer'),
		('d', 'Denied'),
		('r', 'Remove'),
	)

	status = models.CharField(
		max_length=1, 
		choices=APP_STATUS,
		blank=True,
		default='p',
		help_text='Application status')

	class Meta:
		ordering = ['company']

	def __str__(self):
		'''String for representing the Model object'''
		return f'{self.id} ({self.company} {self.position})'

	def get_absolute_url(self):
		'''Returns url to access a detail record for this application'''
		return reverse('applications:application-detail', args=[str(self.id)])
