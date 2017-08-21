from django.contrib import admin
from website.models import Post, Category, Author, Comnt


# Register your models here.
admin.site.register(Post)
admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Comnt)
