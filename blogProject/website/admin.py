from django.contrib import admin
from website.models import Post, Category, Author


# Register your models here.
admin.site.register(Post)
admin.site.register(Author)
admin.site.register(Category)