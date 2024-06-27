from django import forms
from .models import AudioRecording

class AudioRecordingForm(forms.Form):
    audio_file = forms.FileField()
    text = forms.CharField(widget=forms.Textarea, required=False)  # Campo de texto para la descripción

