from django.db import models
from django.contrib.auth.models import AbstractUser
from resources.models import Resource

# Create your models here.

class Profile(AbstractUser):
    goals = models.JSONField(default=list)
    resources = models.ManyToManyField(Resource, related_name='user_resources', blank = True )