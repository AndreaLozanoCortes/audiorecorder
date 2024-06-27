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
            audio_file = form.cleaned_data['audio_file']
            text = form.cleaned_data['text']
            audio_data = audio_file.read()  # Leer los datos binarios del archivo
            audio_recording = AudioRecording(
                audio_file=audio_data,
                text=text
            )
            audio_recording.save()
            #form.save(commit=True)
            return redirect('home')
        else:
            print("Es invalido")
    return redirect('home')

def test(request):
    
    return render(request, 'recorder/test.html')

def download_audio(request, recording_id):
    recording = AudioRecording.objects.get(id=recording_id)
    response = HttpResponse(recording.audio_file, content_type='audio/mpeg')
    response['Content-Disposition'] = f'attachment; text="{recording.text}"'
    return response

