from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from django.shortcuts import redirect
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from .models import Post, Author, Category, Comnt
# from .forms import CommentForm, CommentForm
from django.http import HttpResponse, HttpResponseRedirect
from .forms import CommentCreateForm, CommentNewCreateForm


# from .models import Post, Author, Category, Cmnt
# from .forms import CommentForm

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

def contact(request):
	return render(request, 'website/basic.html', {
		'content': ['Contact me at :','supr.pr@gmail.com']
		})
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
		context['comments'] = Comnt.objects.all()		
		return context


class SinglePostView(DetailView):
	template_name = 'website/singlepost.html'
	model = Post

	def get_context_data(self, **kwargs):
		context = super(SinglePostView, self).get_context_data(**kwargs)
		context['authors'] = Author.objects.all()
		context['comments'] = Comnt.objects.all()		

		return context


class CommentDetailView(DetailView):
	queryset = Comnt.objects.all()


class CommentCreateView(CreateView):
	form_class = CommentNewCreateForm
	template_name = 'website/add_comment.html'
	success_url = "/blog/"








# class ComntView(ListView):
# 	template_name = 'website/comments.html'
# 	model = Comnt




# def comnt_view(request):
	
# 	form = CommentForm(request.POST or None)
# 	model = Comnt

# 	if request.method == 'POST' and form.is_valid():
# 	# if form.is_valid():

# 		user = form.save(commit= False)
# 		a= Comnt.objects.get(pk=1)
# 		form = CommentForm(request.POST, instance=a)


# 		user.save()


# 	context = {
# 			# "form": regform,
# 			"form": form,
# 	}
# 	return render(request, 'website/add_comment.html', context)

















	# return render_to_response(request, 'website/add_comment.html', context)


# def add_comment(request, slug):
# 	post = get_object_or_404(Post, slug=slug)
# 	if request.method == 'POST':
# 		form = CommentForm(request.POST)
# 		if form.is_valid():
# 			commment = form.save(commit=False)
# 			comment.post = post
# 			comment.save()
# 			return redirect('/blog/')
# 			# return redirect('blog:post_detail', slug=post.slug)
# 	else:
# 		form = CommentForm()
# 	template = 'website/add_comment.html'
# 	context = {'form': form}
# 	return render(request, template, context)

# def post_detail(request, slug=None):
# 	isinstance = get _object_or_404(Post, slug=slug)
# 	if isinstance.publish > timezone.now().date() or instance.draft:
# 		if not request.user is_staff or not request.user.is_superuser:
# 			raise Http404
# 	share_string = quote_plus(instance.content)
# 	comments = Comment.objects.filter_by_instance(instance)
# 	context= {
# 		"title": instance.title,
# 		"instance": instance,
# 		"share_string": share_string,
# 		"comments": comments,
# 	}

# 	return render (request, "post_detail.html", context)