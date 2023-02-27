
# Create your views here.
from django.http.response import HttpResponse
from .models import Event
from django.shortcuts import render
from .forms import EvenementForm
from django.views.generic import *
from django.urls import reverse_lazy

def index(request,name):
    return HttpResponse("Rendering "+name)

def list_event(request):
    list=Event.objects.filter(state=True)
    nbr=Event.objects.count()
    return render(request, 'event/list_events.html', {'list':list , 'nbr' :nbr})

class ListEvents(ListView):
    model=Event
    template_name='event/list_events.html'
    context_object_name='list'
    # paginate_by=2
    
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['nbr']=Event.objects.count()
        return context
    def  get_queryset(self):
        eventsTrue=Event.objects.filter(state=True)
        return eventsTrue

#method 1 using class based view
class AddEvent(CreateView):

    template_name = "event/addEvent.html"
    model = Event
    form_class = EvenementForm
    success_url = reverse_lazy('Affiche')

#method 2 using custom function
def AddEv(req):
    form=EvenementForm()
    if req.method=='POST':
         form=EvenementForm(req.POST , req.FILES)
         if form.is_valid():
                form.save()
                return HttpResponse("Event Added")
    return render(req,'event/addEvent.html',{'form':form})

class UpdateEvent(UpdateView):
    template_name = "event/updateEvent.html"
    model = Event
    form_class = EvenementForm
    success_url = reverse_lazy('Affiche')

class DeleteEvent(DeleteView):
    model = Event
    template_name = "event/deleteEvent.html"
    success_url = reverse_lazy('Affiche')
