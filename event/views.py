
# Create your views here.
from django.http.response import HttpResponse
from .models import Event
from django.shortcuts import render

def index(request,name):
    return HttpResponse("Rendering "+name)

def list_event(request):
    list=Event.objects.all()
    return render(request, 'event/list_events.html', {'list':list})