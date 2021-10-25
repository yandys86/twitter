from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.


class Post(models.Model):
    class Meta(object):
        db_table = 'post'
    name = models.CharField(
        'Name', blank=False, null=False, max_length=14, db_index=True, default='Anonymus'
    )
    body = models.CharField(
        'Body', blank=False, null=False, max_length=140, db_index=True
    )
    created_at = models.DateTimeField(
        'Created_ DateTime', blank=True, auto_now=True
    )
    image = CloudinaryField(
        'Image', blank=True, null=True
    )
    like_count=models.IntegerField('LikeCount',default=0,blank=True)
    

    def __str__(self):
        return self.name


# class Photo(models.Model):
 #   image = CloudinaryField('image')
