from django.db import models


class Song(models.Model):
    artist = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    cover = models.ImageField()
    song = models.FileField()
    
    def __str__(self):
        return "{} - {}".format(self.artist, self.title)
