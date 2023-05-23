from django.db import models
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
        return reverse('post_list', args=(str(self.id)))

class Post(models.Model):

    #Save posts as draft until ready to publish
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    title = models.CharField(max_length=255)
    #related_name allows us to access related objects from a user object, like user.blog_posts
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    slug = models.SlugField(max_length=255, unique_for_date='publish')
    body = models.TextField()
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
        return reverse('MainApp:post_detail', args=[self.publish.year,
                                                    self.publish.month,
                                                    self.publish.day,
                                                    self.slug])

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
    body = models.TextField()

    class Meta:
        ordering = ['created']
        indexes = [models.Index(fields=['created']),]

    def __str__(self):
        return f'Comment by {self.body}'