from django.contrib import admin
from .models import Post, Debate, Category, Comment

admin.site.register(Post)
admin.site.register(Debate)
admin.site.register(Category)
admin.site.register(Comment)