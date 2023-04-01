from django.db import models
from django.contrib.auth.models import AbstractUser
from resources.models import Resource


class Profile(AbstractUser):
    """
    Represents a Profile for an authenticated
    user.
    Extends Django's User class to include details
    such as Goals and Resources.
    """
    goals = models.JSONField(default=list)
    resources = models.ManyToManyField(
        Resource, related_name="user_resources", blank=True
    )
