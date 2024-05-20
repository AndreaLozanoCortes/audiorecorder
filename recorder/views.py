from django.shortcuts import render, redirect
from .forms import AudioRecordingForm
from .models import AudioRecording
from django.http import FileResponse
from django.http import HttpResponse

def home(request):
    form = AudioRecordingForm()
    recordings = AudioRecording.objects.all()
    return render(request, 'recorder/home.html', {'form': form, 'recordings': recordings})

def save_audio(request):
    if request.method == 'POST':
        print(request.POST)
        print(request.FILES)
        
        form = AudioRecordingForm(request.POST, request.FILES)
        
        if form.is_valid():
            print("Es valido")
            form.save(commit=True)
            return redirect('home')
        else:
            print("Es invalido")
    return redirect('home')

def test(request):
    
    return render(request, 'recorder/test.html')

def download_audio(request, recording_id):
    recording = AudioRecording.objects.get(id=recording_id)
    audio_file = recording.audio_file
    response = FileResponse(open(audio_file.path, 'rb'), content_type='audio/mpeg')
    #response = HttpResponse(recording.audio_file, content_type='audio/mpeg')
    return response