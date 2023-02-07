from django.contrib import admin
from .models import Event, Participants
# Register your models here.

# admin.site.register(Event)

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display={
        'title','description','image','categoy','state',
        'nbr_participant','evt_date','created_date','updated_date','participant','organisateur'
    }
    list_display=[field.name for field in Event._meta.get_fields()]

admin.site.register(Participants)
