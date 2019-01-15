from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
	path('', views.homepage, name='homepage'),
	path('signup/', views.signup, name='signup'),
	path('edit_user/', views.edit_user, name='edit-user'),
	# path('homepage/<int:pk>', views.UserDetailView.as_view(), name='user-detail'),
]