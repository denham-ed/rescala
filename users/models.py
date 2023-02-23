from django.db import models
from django.contrib.auth.models import AbstractUser
from resources.models import Resource


class Profile(AbstractUser):
    goals = models.JSONField(default=list)
    resources = models.ManyToManyField(Resource, related_name='user_resources', blank = True )