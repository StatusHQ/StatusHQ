from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
	path('applications/all', views.AllApplicationsListView.as_view(), name='applications-all'),
	path('applications/past/', views.PastApplicationsListView.as_view(), name='applications-past'),
	path('applications/current/', views.CurrentApplicationsListView.as_view(), name='applications-current'),
	path('applications/<int:pk>', views.ApplicationDetailView.as_view(), name='application-detail'),
	path('applications/create/', views.ApplicationCreate.as_view(), name='application-create'),
	path('applications/<int:pk>/update/', views.ApplicationUpdate.as_view(), name='application-update'),
	path('applications/<int:pk>/delete/', views.ApplicationDelete.as_view(), name='application-delete'),
	path('applications/<int:pk>/change_status/', views.ChangeStatus.as_view(), name='change-status'),
]