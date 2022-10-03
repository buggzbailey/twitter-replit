from django.db import models
from cloudinary.models import CloudinaryField


class Post(models.Model):
    class Meta(object):
        db_table = 'posts'

    name = models.CharField(
        'name', blank=False, null=False, max_length=14, db_index=True, default='anonymous'
    )
    body = models.CharField(
        'body', blank=True, null=True, max_length=240, db_index=True
    )
    created_at = models.DateTimeField(
        'Created DateTime', blank=True, auto_now_add=True
    )
# add image
    image = CloudinaryField(
        'Image', blank=True, null=True
    )

    updated_at = models.DateField(
        'Updated DateTime', blank=True, auto_now_add=True)

    like_count = models.PositiveIntegerField(
        'Like Count', default=0, blank=True
    )
