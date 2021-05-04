from django.db import models
from embed_video.fields import EmbedVideoField


# Create your models here.

class Item(models.Model):
    video = EmbedVideoField()  # same like models.URLField()


class Video(models.Model):
    caption=models.CharField(max_length=100)
    video=models.FileField(upload_to="video/%y")
    def __str__(self):
        return self.caption
