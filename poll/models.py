from django.contrib.auth.models import User
from django.db import models
from MainApp.models import Category

class Poll(models.Model):
    title = models.CharField(max_length=255)
    published = models.DateTimeField('Date Published')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, related_name="categories")



class Choice(models.Model):
    poll = models.ForeignKey(Poll, null=True, on_delete=models.CASCADE)
    choice = models.CharField(max_length=255)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice

class Vote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)

    class Meta:
        unique_together = ['user', 'choice']