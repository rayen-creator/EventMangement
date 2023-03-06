
# Create your views here.
from django.http.response import HttpResponse
from .models import *
from django.shortcuts import redirect, render
from .forms import EvenementForm
from django.views.generic import *
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Person


def index(request, name):
    return HttpResponse("Rendering "+name)


@login_required
def list_event(request):
    list = Event.objects.filter(state=True)
    nbr = Event.objects.count()
    return render(request, 'event/list_events.html', {'list': list, 'nbr': nbr})


class ListEvents(LoginRequiredMixin, ListView):
    model = Event
    template_name = 'event/list_events.html'
    context_object_name = 'list'
    # paginate_by=2
    login_url = 'login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['nbr'] = Event.objects.count()
        return context

    def get_queryset(self):
        eventsTrue = Event.objects.filter(state=True)
        return eventsTrue

# method 1 using class based view


class AddEvent(CreateView):

    template_name = "event/addEvent.html"
    model = Event
    form_class = EvenementForm
    success_url = reverse_lazy('Affiche')

# method 2 using custom function


def AddEv(req):
    form = EvenementForm()
    if req.method == 'POST':
        form = EvenementForm(req.POST, req.FILES)
        if form.is_valid():
            form.instance.organisateur = Person.objects.get(cin=req.user.cin)
            form.save()
            return HttpResponse("Event Added")
    return render(req, 'event/addEvent.html', {'form': form})


class UpdateEvent(UpdateView):
    template_name = "event/updateEvent.html"
    model = Event
    form_class = EvenementForm
    success_url = reverse_lazy('Affiche')


class DeleteEvent(DeleteView):
    model = Event
    template_name = "event/deleteEvent.html"
    success_url = reverse_lazy('Affiche')


class DetailsEvent(DetailView):
    model = Event
    template_name = "event/details.html"
    context_object_name = "event"  # par défaut object_list


def detailsss(req, pk):

    event = Event.objects.get(id=pk)

    return render(req, "event/details.html", {'e': event})


def participer(request, event_id):
    user = request.user
    event = Event.objects.get(id=event_id)
    participant = Participants.objects.create(
        personne=user, event=event
    )
    participant.save()
    event.nbr_participant += 1
    event.save()
    return redirect('Affiche')

def cancel (req,event_id):
    user=req.user
    event=Event.objects.get(id=event_id)
    participant=Participants.objects.get(personne=user,event=event)
    participant.delete()
    event.nbr_participant -= 1
    event.save()
    return redirect('Affiche')

def eventDetails(request, event_id):
    user=request.user
    event=Event.objects.get(event_id=id)
    if user:
          participant=Participants.objects.get(personne=user,event=event)
    if participant:
        button_disabled=True
    else:
        button_disabled=False
    return render(req,'event/details.html',{'e':event,'button_disabled':button_disabled})