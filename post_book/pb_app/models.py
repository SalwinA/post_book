from django.db import models
from datetime import datetime


# Create your models here.
class user_profile(models.Model):
    user = models.CharField(max_length=40, null=False, blank=False)
    email = models.CharField(max_length=40, null=False, blank=False)
    password = models.CharField(max_length=40, null=False, blank=False)
    
    def __str__(self):
        return self.user.username


class user_post(models.Model):
    user = models.CharField(max_length=50)
    post_text = models.TextField()
    post_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.user