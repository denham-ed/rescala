from django.db import models
from django.contrib.auth.models import User
from users.models import Profile
from cloudinary.models import CloudinaryField
from . import validators



class Session(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, name='user')
    date = models.DateField(validators=[validators.validate_date])
    duration = models.IntegerField(validators=[validators.validate_duration])
    headline = models.CharField(max_length=150)
    image = CloudinaryField('image', blank=True)
    focus = models.JSONField(default=list, blank=True)
    moods = models.JSONField(default=list, blank=True)
    summary = models.TextField()
