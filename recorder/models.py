from django.db import models

class AudioRecording(models.Model):
    audio_file = models.BinaryField(editable=True)
    text = models.TextField(default='')
    timestamp = models.DateTimeField(auto_now_add=True)
    
    #name = models.CharField(max_length=255)
    def __str__(self):
        return f"AudioRecording {self.id}"
