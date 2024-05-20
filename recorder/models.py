from django.db import models

class AudioRecording(models.Model):
    audio_file = models.FileField(upload_to='audio_recordings/')
    timestamp = models.DateTimeField(auto_now_add=True)
    #name = models.CharField(max_length=255)
    def __str__(self):
        return f"AudioRecording {self.id}"
