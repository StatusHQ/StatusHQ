from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
	path('', views.homepage, name='homepage'),
	path('signup/', views.signup, name='signup'),
]