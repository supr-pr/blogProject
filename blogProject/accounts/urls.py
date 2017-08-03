
from django.conf.urls import url, include
from . import views
from django.contrib.auth import views as auth_views
from django.contrib import admin
from accounts.views import (login_view, register_view, logout_view, actions_view)

urlpatterns = [
	url(r'^login/$', login_view),
	url(r'^logout/$', logout_view),
	url(r'^register/$', register_view),
	url(r'^actions/$', actions_view),
	url('^', include('django.contrib.auth.urls')),

	# url(r'^password_reset/$', auth_views.password_reset, name='password_reset'),
 #    url(r'^password_reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
 #    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
 #        auth_views.password_reset_confirm, name='password_reset_confirm'),
    # url(r'^reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),
    # url(r'^reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),
    
]
