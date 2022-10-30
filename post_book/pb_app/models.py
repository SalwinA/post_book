from django.db import models


# Create your models here.
class user_profile(models.Model):
    user = models.CharField(max_length=40, null=False, blank=False)
    email = models.CharField(max_length=40, null=False, blank=False)
    password = models.CharField(max_length=40, null=False, blank=False)
    
    def __str__(self):
        return self.user.username