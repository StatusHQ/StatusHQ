# -*- coding: utf-8 -*-
# @Author: Charlie Gallentine
# @Date:   2018-12-17 12:44:03
# @Last Modified by:   Charlie Gallentine
# @Last Modified time: 2018-12-18 21:39:35
from django.urls import path
from . import views
from django.conf.urls import url

app_name = 'prof_profile'

urlpatterns = [
	path('', views.index, name='index'),
	path('<int:section_id>/', views.prof_section, name='prof_section'),
	path('create/', views.prof_add_section, name='prof_add_section'),
	path('remove/', views.prof_del_section, name='prof_del_section'),
	path('<int:section_id>/add/', views.prof_section_add_exp, name='prof_section_add_exp'),
	path('<int:section_id>/delete/', views.prof_section_del_exp, name='prof_section_del_exp'),
]