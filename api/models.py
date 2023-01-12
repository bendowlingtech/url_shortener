from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

from django.db import models

class URL(models.Model):
    original_url = models.TextField()
    key = models.TextField(unique=True)
    secret_key = models.TextField(unique=True)
    is_active = models.BooleanField(default=True)
    clicks = models.IntegerField(default=0)

class CustomUser(AbstractUser):
    pass
    # add additional fields in here

    def __str__(self):
        return self.username











