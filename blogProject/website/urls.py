from django.conf.urls import url, include
from . import views
from website.views import Home_View, SinglePostView, BlogListView
from website.models import Post, Category, Author, Comnt
# from website.models import Post, Category, Author, Cmnt
# from django.contrib import admin

from django.contrib.auth import views as auth_views

from website.views import (
	# resturant_listview,
	# , comnt_view
	# ResturantListView,
	CommentDetailView,
	# resturant_create_view
	CommentCreateView

)

# admin.autodiscover()

urlpatterns = [

    # url(r'^$', views.index, name = 'index'),
    # url(r'^contact/', views.contact, name = 'contact'),
	#url(r'^$', ListView.as_view(queryset=Post.objects.all().order_by("-date")[:25],template_name="blog/blog.html")),url(r'^(?P<pk>\d+)$', DetailView.as_view(model = Post, template_name = 'blog/post.html'))
    url(r'^blog/$', views.BlogListView.as_view(), name = 'index'),
	url(r'^$', Home_View),
    url(r'^contact/', views.contact, name = 'contact'),
	url(r'^blog/(?P<pk>\d+)$', views.SinglePostView.as_view(), name = 'singlPst'),
	# url(r'^blog/\d+/comnt/$', comnt_view),
    url(r'^blog/\d+/comnt/$', CommentCreateView.as_view()),
    url(r'^comnt/$', CommentDetailView.as_view()),


    # url(r'^blog/(?P<pk>\d+)/comnt/$', views.ComntView.as_view(), name = 'Comnt'),

    # url(r'^blog/(?P<pk>\d+<slug>[-\w]+)/comment/$', views.add_comment)
   

]



# urlpatterns = patterns('',
#    url(r'^$', 'thirdauth.views.home', name='home'),
# )