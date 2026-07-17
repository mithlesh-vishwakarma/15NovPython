from django.shortcuts import render,HttpResponse
from playlists.urls import *
# Create your views here.

def home(request):
  # return HttpResponse("Welcome to my Spotify Playlists")
  return HttpResponse("mithlesh")