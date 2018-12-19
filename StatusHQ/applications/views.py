from django.shortcuts import render, get_object_or_404
from applications.models import Application 
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from applications.models import Application 
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect

class AllApplicationsListView(LoginRequiredMixin, generic.ListView):
	'''Generic class-based view listing user applications'''
	model = Application 
	context_object_name = 'applications_list'
	template_name = 'applications/applications_home.html'
	paginate_by = 10

	def get_queryset(self):
		return Application.objects.filter(owner=self.request.user).order_by('status')

class CurrentApplicationsListView(LoginRequiredMixin, generic.ListView):
	model = Application 
	context_object_name = 'applications_list'
	template_name = 'applications/applications_home.html'
	paginate_by = 10

	def get_queryset(self):
		return Application.objects.filter(owner=self.request.user, status__in=['p', 'i', 'o', 'a']).order_by('date_applied')

class PastApplicationsListView(LoginRequiredMixin, generic.ListView):
	model = Application 
	context_object_name = 'applications_list'
	template_name = 'applications/applications_home.html'
	paginate_by = 10

	def get_queryset(self):
		return Application.objects.filter(owner=self.request.user, status__in=['r', 'd']).order_by('date_applied')

class ApplicationDetailView(LoginRequiredMixin, generic.DetailView):
	model = Application


class ApplicationCreate(LoginRequiredMixin, CreateView):
	model = Application
	fields = ['company', 'position', 'date_applied', 'deadline', 'status']

	def form_valid(self, form):
		form.instance.owner = self.request.user
		return super().form_valid(form)

class ApplicationUpdate(LoginRequiredMixin, UpdateView):
	model = Application 
	fields = ['company', 'position', 'date_applied', 'deadline', 'status']

class ApplicationDelete(LoginRequiredMixin, DeleteView):
	model = Application
	success_url = reverse_lazy('applications')

class ChangeStatus(LoginRequiredMixin, generic.View):
	def post(self, request, *args, **kwargs):
		application = Application.objects.filter(id=self.kwargs['pk']).update(status=request.POST.get("status"))
		return HttpResponseRedirect('/applications/applications/current/')

