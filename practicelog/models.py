from django.db import models
from django.contrib.auth.models import User
from users.models import Profile
from cloudinary.models import CloudinaryField



class Session(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, name='sessions')
    date = models.DateTimeField()
    duration = models.IntegerField()
    headline = models.TextField()
    image = CloudinaryField('image')
    focus = models.JSONField(default=list)
    summary = models.TextField()
    focus = models.JSONField(default=list)
