
from django.conf.urls import url, include
from . import views
from website.views import Home_View, SinglePostView, BlogListView
from website.models import Post, Category, Author
from django.contrib.auth import views as auth_views

urlpatterns = [

    # url(r'^$', views.index, name = 'index'),
    # url(r'^contact/', views.contact, name = 'contact'),
	#url(r'^$', ListView.as_view(queryset=Post.objects.all().order_by("-date")[:25],template_name="blog/blog.html")),url(r'^(?P<pk>\d+)$', DetailView.as_view(model = Post, template_name = 'blog/post.html'))
    url(r'^blog/$', views.BlogListView.as_view(), name = 'index'),
	url(r'^$', Home_View),
	url(r'^blog/(?P<pk>\d+)$', views.SinglePostView.as_view(), name = 'singlPst')
]
