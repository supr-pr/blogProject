from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from .models import Post, Author, Category

# Create your views here.
# def index(request):
#     return render (request, 'website/header.html')


def Home_View(request):
	template_name = "website/header.html"
	queryset = Post.objects.all()
	context_object_name = 'Posts'
	context ={
		 "object_list": queryset
	}
	return render(request, template_name, context)


# class Blog_View(ListView):
# 	"""docstring for ClassName"""
# 	# def __init__(self, arg):
# 	# 	super(ClassName, self).__init__()
# 	# 	self.arg = arg

# 	model = Post
# 	context_object_name = 'Posts'
# 	queryset = Post.objects.all()
# 	template_name = "website/home.html"
class BlogListView(ListView):
	template_name = 'website/home.html'
	model = Post

	def get_context_data(self, **kwargs):
		context = super(BlogListView, self).get_context_data(**kwargs)
		context['categories'] = Category.objects.all()
		return context


class SinglePostView(DetailView):
	template_name = 'website/singlepost.html'
	model = Post

	def get_context_data(self, **kwargs):
		context = super(SinglePostView, self).get_context_data(**kwargs)
		context['authors'] = Author.objects.all()
		return context

