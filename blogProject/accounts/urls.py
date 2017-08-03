
from django.conf.urls import url, include
from . import views
from django.contrib.auth import views as auth_views
from django.contrib import admin
from accounts.views import (login_view, register_view, logout_view)

urlpatterns = [
	url(r'^login/$', login_view),
	url(r'^logout/$', logout_view),
	url(r'^register/$', register_view),

]
