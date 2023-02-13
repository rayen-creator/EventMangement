from django.contrib import admin
from .models import Event, Participants
# Register your models here.

# admin.site.register(Event)

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display=(
        'title','description','image','categoy','state',
        'nbr_participant','evt_date','created_date','updated_date','e','organisateur'
    )
    list_per_page=2
    ordering=['title']
    # list_display=[field.name for field in Event._meta.get_fields()]
    def e(self,obj):
        count=obj.participant.count()
        return count
    e.short_description='nombre participant'

    def participant(self):
        return "\n".join([p.participants for p in self.participant.all()])
admin.site.register(Participants)
