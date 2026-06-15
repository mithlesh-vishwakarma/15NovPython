from django.shortcuts import render
from django.http import HttpResponse # Import HttpResponse to return HTML responses

# Create your views here.

def home(request):
    """
    A simple Django view function.
    
    Arguments:
        request: The HTTP Request object sent by the browser.
        
    Returns:
        HttpResponse: A simple HTTP response with a greeting message.
    """
    # Returns the welcome message with Mithlesh's name
    return HttpResponse("Welcome to My Spotify Playlists! - Mithlesh")
