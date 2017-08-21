"""thirdauth URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import include, url
# from django.conf.urls.defaults import *

from thirdauth.views import (
	home,

)

# admin.autodiscover()

# urlpatterns = patterns('',
#    url(r'^auth/$', 'thirdauth.views.home', name='home'),
# )

urlpatterns = [

   # url(r'^auth/$', 'thirdauth.views.home', name='home'),
   url(r'^auth/$', home),
   url('', include('social.apps.django_app.urls', namespace='social')),
	url('', include('django.contrib.auth.urls', namespace='auth')),
]

