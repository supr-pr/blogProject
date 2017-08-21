from django.db import models
from django.forms import ModelForm
from django.conf import settings
from  django.contrib.contenttypes.fields import GenericForeignKey
from  django.contrib.contenttypes.models import ContentType
# from comments.models import Comment


# @property
# def commens(self):
# 	qs = Comment.objects.filter_by_instance(instance)
# 	return qs


class Category(models.Model):
	category = models.CharField(max_length=100, default='Blog')
	def __str__ (self):
		return self.category

class Author(models.Model):
	author = models.CharField(max_length=100, default='Anonymous')
	def __str__(self):
		return self.author


# class Cmnt(models.Model):
# title = models.CharField(max_length=100)
# 	date = models.DateTimeField()
# user = models.ForeignKey(Author)
# 	user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
# 	content_type = models.ForeignKey(ContenType, on_delete= models.CASCADE)
# 	object_id = models.PositiveIntegerField()
# 	comment_object = GenericForeignKey('content_type', 'object_id')
# 	content = models.TextField()
# 	timestamp = models.DateTimeField(auto_now_add=True)


# 	objects = CommentManager()
# 	# def get_fields_and_values(self):
#  #            return [(field, field.value_to_string(self)) for field in Post._meta.fields]
# 	def __str__ (self):
# 		return str(self.user.username)
# 		# return self.author


# class CommentManager(models.Manager):
# 	def filter_by_instance(self,instance):
# 		content_type = ContenType.objects.get_for_model(instance, __class__)
# 		obj_id = instance.obj_id
# 		# comments = Comment.objects.filter(content_type=content_type, obj_id= obj_id)
# 		qs = super (CommentManager, self).filter(content_type=content_type, object_id=obj_id)
# 		# comments = Comment.objects.filter(content_type=content_type, object_id=obj_id)
# 		return qs


class Post(models.Model):
	title = models.CharField(max_length=100)
	body = models.TextField()
	date = models.DateTimeField()
	author = models.ForeignKey(Author)
	category = models.ForeignKey(Category)
	# cmnt = models.ForeignKey(Cmnt)

	# def get_fields_and_values(self):
 #            return [(field, field.value_to_string(self)) for field in Post._meta.fields]

	def __str__ (self):
		return self.title



class Comnt(models.Model):
	content = models.TextField(default='')
	# date = models.DateTimeField(auto_now=True, auto_now_add=False)
	date = models.DateTimeField(auto_now_add=True)
	author = models.ForeignKey(Author)
	comnt_on = models.ForeignKey(Post)
	updated 		= models.DateTimeField(auto_now=True)
	my_date_field 	= models.DateTimeField(auto_now=True, auto_now_add=False)

	def __str__ (self):
		return self.content

	@property
	def title(self):
		return self.content 

class ComntForm(ModelForm):
	class Meta:
		model = Comnt
		fields = [
			'content',
			'author',
			# 'email2'
			'comnt_on'
		]