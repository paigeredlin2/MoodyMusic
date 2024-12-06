from django.shortcuts import render, redirect
import json
from django.contrib import messages
from .models import Song
from .serializers import SongSerializer
from .forms import FeedbackForm
# Create your views here.
# Using serializers to make the query_set a usable array for use in templates
def home_view(request):
    return render(request, 'player/home.html')

def form_view(request):
    form = FeedbackForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Thank you for your feedback!')
        return redirect('home')
    return render(request, 'player/request.html', {'form': form})

def classical_view(request):
    query_set = Song.objects.filter(playlist = "Classical")
    song_list = json.dumps(SongSerializer(query_set, many=True).data)
    return render(request, 'player/audio.html',{'song_list': song_list})

def lofi_view(request):
    query_set = Song.objects.filter(playlist = "Lofi")
    song_list = json.dumps(SongSerializer(query_set, many=True).data)
    return render(request, 'player/audio.html', {'song_list': song_list})

def videogame_view(request):
    query_set = Song.objects.filter(playlist = "Video Game")
    song_list = json.dumps(SongSerializer(query_set, many=True).data)
    return render(request, 'player/audio.html', {'song_list': song_list})

