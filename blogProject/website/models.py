from django.db import models

class Category(models.Model):
	category = models.CharField(max_length=100, default='Blog')
	def __str__ (self):
		return self.category

class Author(models.Model):
	author = models.CharField(max_length=100, default='Anonymous')
	def __str__(self):
		return self.author


class Post(models.Model):
	title = models.CharField(max_length=100)
	body = models.TextField()
	date = models.DateTimeField()
	author = models.ForeignKey(Author)
	category = models.ForeignKey(Category)
	# def get_fields_and_values(self):
 #            return [(field, field.value_to_string(self)) for field in Post._meta.fields]

	def __str__ (self):
		return self.title