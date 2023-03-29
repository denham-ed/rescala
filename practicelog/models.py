from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from users.models import Profile
from . import validators


class Session(models.Model):
    """
    Represents a session recorded by the user, with details such as the date,
    duration, headline, image, areas of focus , moods, and a summary of the
    session.
    """
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, name='user')
    date = models.DateField(validators=[validators.validate_date])
    duration = models.IntegerField(validators=[validators.validate_duration])
    headline = models.CharField(max_length=150)
    image = CloudinaryField('image', blank=True)
    focus = models.JSONField(default=list, blank=True)
    moods = models.JSONField(default=list, blank=True)
    summary = models.TextField()
