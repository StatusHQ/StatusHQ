"""StatusHQ URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # add url to redirect the base url to our homepage app
    path('', RedirectView.as_view(url='/homepage/', permanent=True)),

    # forwards requests with the pattern homepage/ to our homepage application
    path('homepage/', include('homepage.urls')),

    # forwards requests to applications app
    path('applications/', include('applications.urls')),

    # add django auth urls for login, logour, and password management
    path('accounts/', include('django.contrib.auth.urls')),
]
