from django.db import models
from django.contrib.auth.models import User
from users.models import Profile
from cloudinary.models import CloudinaryField



class Session(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, name='user')
    date = models.DateField()
    duration = models.IntegerField()
    headline = models.CharField(max_length=150)
    image = CloudinaryField('image', blank=True)
    focus = models.JSONField(default=list, blank=True)
    moods = models.JSONField(default=list, blank=True)
    summary = models.TextField()
