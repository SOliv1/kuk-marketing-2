from video.apps import VideoConfig
from django.db import models



# Create your models here.

class Item(models.Model):
    video = VideoConfig()  # same like models.URLField()


class Video(models.Model):
    caption=models.CharField(max_length=100)
    video=models.FileField(upload_to="video/%y")
    def __str__(self):
        return self.caption
