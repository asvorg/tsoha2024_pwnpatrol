from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    role = models.CharField(max_length=255, default='user')  # role: user/admin
    organization = models.ForeignKey('organizations.Organization', on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return self.username
