from django.db import models
from django.contrib.auth.models import User
import re
def video_directory_path(instance, filename):
	return 'video/{0}'.format(filename)
def audio_directory_path(instance, filename):
    return 'audio/{0}'.format(filename)
class Video(models.Model):
    name = models.CharField(max_length=100)
    video_file = models.FileField(upload_to=video_directory_path, default="video_example.mp4")
    audio_file = models.FileField(upload_to=audio_directory_path,blank=True, null=True)
    slug = models.SlugField(null=True, blank=True)
    whisper_transcribe = models.TextField(null=True, blank=True)
    whisper_summary = models.TextField(null=True, blank=True)
    whisper_transcribe_translate = models.TextField(null=True, blank=True)
    whisper_summary_translate = models.TextField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.name}"