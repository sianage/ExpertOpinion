from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from ckeditor.fields import RichTextField

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Post.Status.PUBLISHED)

class Category(models.Model):
    category = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.category

    #may need get_absolute_url function
    def get_absolute_url(self):
        return reverse('home', args=(str(self.id)))

class Post(models.Model):

    #Save posts as draft until ready to publish
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    title = models.CharField(max_length=255)
    header_image = models.ImageField(null=True, blank=True, upload_to="images/profile/")
    #related_name allows us to access related objects from a user object, like user.blog_posts
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    slug = models.SlugField(max_length=255, unique_for_date='publish')
    body = RichTextField(blank=True, null=True)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    #auto_now automatically updates the date when saving
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="posts")

    #default manager
    objects = models.Manager()
    #custom manager
    published = PublishedManager()

    #displays blog posts from newest to oldest
    class Meta:
        ordering = ['-publish']
        #DB index (speeds up data retrieval operations)
        indexes = [models.Index(fields=['-publish']),]

    def __str__(self):
        return self.title + ' by ' + str(self.author)

    def get_absolute_url(self):
        return reverse('MainApp:post_detail', args=(str(self.id)))

class Debate(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="debates")
    title = models.CharField(max_length=255)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']
        indexes = [models.Index(fields=['created']),]

    def __str__(self):
        return f'Comment by {self.title}'

class Comment(models.Model):
    debate = models.ForeignKey(Debate, on_delete=models.CASCADE, related_name="comments")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    commenter_name = models.ForeignKey(User, on_delete=models.CASCADE)
    #form.media in view (tut 21)
    body = RichTextField(blank=True, null=True)

    class Meta:
        ordering = ['created']
        indexes = [models.Index(fields=['created']),]

    def __str__(self):
        return f'Comment by {self.body}'

class Profile(models.Model):
    field1 = "philosophy"
    field2 = "economics"
    field3 = "medicine"
    field4 = "political_science"

    fields = ((field1, 'Philosophy'), (field2, "Economics"),
              (field3, "Medicine"), (field4, "Political Science"),)

    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    field = models.CharField(max_length=30, choices=fields, default="No Field Selected")
    bio = models.TextField(default='')
    profile_picture = models.ImageField(null=True, blank=True, upload_to="images/profile/")
    github_url = models.CharField(max_length=255, null=True, blank=True)
    linkedin_url = models.CharField(max_length=255, null=True, blank=True)
    def __str__(self):
        return f"Academic field of user: {self.field}"

    def get_absolute_url(self):
        return reverse('MainApp:profile_view', args=[self.user.primary_key])