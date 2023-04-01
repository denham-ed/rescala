from django.db import models
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))


class Resource(models.Model):
    """
    Represents a Resource added by the Admin.
    Details include title, content, image, excerpt and status.
    The slug and created_on attributes are auto-generated.
    A default featured image is provided.

    Resources are sorted by created on date.
    """

    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    content = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(max_length=300)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']
    
    def __str__(self):
        return self.title
