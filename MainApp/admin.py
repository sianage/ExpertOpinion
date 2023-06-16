from django.contrib import admin
from django.contrib.auth.models import Group, User
from .models import Post, Debate, Category, Comment, Profile, Note

admin.site.register(Post)
admin.site.register(Debate)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.unregister(Group)
admin.site.register(Note)

#add profile info in with User
class ProfileInline(admin.StackedInline):
    model = Profile

class UserAdmin(admin.ModelAdmin):
    model = User
    fields = ["username"]
    inlines = [ProfileInline]

admin.site.unregister(User)
admin.site.register(User, UserAdmin)