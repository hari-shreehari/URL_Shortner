from django.db import models

# Create your models here.

# urlshort/models.py
from django.contrib.auth.models import User
from django.db import models
class URL(models.Model):
    long_url = models.URLField(unique=True)
    short_url = models.CharField(max_length=20, unique=True)

class UrlModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    original_url = models.URLField()
    short_url = models.CharField(max_length=20, unique=True)
