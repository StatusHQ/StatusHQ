from django.shortcuts import render, get_object_or_404
from applications.models import Application 
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from applications.models import Application 
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django import forms 
from .models import ProfileSection, ProfileEntry

class IndexView(LoginRequiredMixin, generic.ListView):
	'''Generic class-based view listing user applications'''
	model = ProfileSection 
	context_object_name = 'sections'
	template_name = 'prof_profile/index.html'
	paginate_by = 10

	def get_queryset(self):
		return ProfileSection.objects.filter(owner=self.request.user)


def prof_section(request, section_id):
	'''Individual section view for categories in profile'''
	section = get_object_or_404(ProfileSection, pk=section_id)

	context = {
		'section': section,
	}

	return render(request, 'prof_profile/prof_section.html', context)

def prof_add_section(request):
	'''Adds a section to the professional profile'''
	section = ProfileSection(section_name=request.POST['section_name'], owner=request.user)
	section.save()
	return HttpResponseRedirect('/prof_profile')

def prof_del_section(request):
	'''Delete section from professional profile'''
	section = ProfileSection(pk=request.POST['pk'])

	for entry in section.profileentry_set.all():
		entry.delete()

	section.delete()
	return HttpResponseRedirect('/prof_profile')

def prof_section_add_exp(request, section_id):
	'''Add an experience to a section in profile'''
	section = get_object_or_404(ProfileSection, pk=section_id)
	try:
		section.profileentry_set.create(
			entry_name=request.POST['experience'],
			entry_text=request.POST['exp_description'])
	except (ValueError, section.DoesNotExist):
		return render(request, 'prof_profile/prof_section.html', {
			'section' : section,
			'error_message' : "Section Does not exist.",
		})
	else:
		section.save()
		return HttpResponseRedirect(reverse('prof_profile:prof_section', args=(section.id,)))

def prof_section_del_exp(request, section_id):
	'''Delete experience from profile'''
	section = get_object_or_404(ProfileSection, pk=section_id)
	try:
		selected_choice = section.profileentry_set.get(pk=request.POST['pk'])
	except (KeyError, ProfileEntry.DoesNotExist):
		# Redisplay the question voting form.
		return render(request, 'prof_profile/prof_section.html', {
			'section': section,
			'error_message': str(section_id) + ": doesn't exist.",
		})
	else:
		selected_choice.delete()
		section.save()
		return HttpResponseRedirect(reverse('prof_profile:prof_section', args=(section.id,)))






















