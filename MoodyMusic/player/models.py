from django.db import models

# Create your models here.
class Song(models.Model):
    song_name = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    playlist = models.CharField(max_length=100)
    cover_image = models.ImageField(upload_to="images")
    audio = models.FileField(upload_to="audio")

class Feedback(models.Model):
    request_user_email = models.EmailField()
    request_song = models.CharField(max_length=100)
    request_artist = models.CharField(max_length=100)
    request_remarks = models.CharField(max_length=10000)