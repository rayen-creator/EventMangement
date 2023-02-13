from django.contrib import admin , messages
from .models import Event, Participants
# Register your models here.



class ParticipantsInline(admin.TabularInline):
    model = Participants
    # readonly_fields=('date_creation',)
    extra=1
    can_delete=True
    classes=['collapse']

def set_Refuse(ModelAdmin,request,queryset):
    rows_updated=queryset.update(state=False)
    if (rows_updated==1):
        message_bit="1 event was"
    else:
        message_bit=f"{rows_updated} events were"
    messages.success(request,f'{message_bit} successfully updated !')

def set_Accept(ModelAdmin,request,queryset):
    rows_updated=queryset.update(state=True)
    if (rows_updated==1):
        message_bit="1 event was"
    else:
        message_bit=f"{rows_updated} events were"
    messages.success(request ,f'{message_bit} successfully updated !')


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display=(
        'title','description','image','categoy','state',
        'nbr_participant','evt_date','created_date','updated_date','e','organisateur'
    )

    list_filter=('title','categoy','state','organisateur')

    actions=[set_Accept,set_Refuse]
    
    actions_on_bottom=True
    
    autocomplete_fields=['organisateur']

    inlines=[ParticipantsInline]

    readonly_fields=('created_date','updated_date')

    fieldsets=(
        ('Event Information',{
            'fields':('title','description','image','categoy','state','nbr_participant','organisateur')
        })   ,
        ('Dates' ,{
            'fields':('evt_date','created_date','updated_date')
        }) 
    )

    list_per_page=2
    ordering=['title'] 

    def e(self,obj):
        count=obj.participant.count()
        return count
    e.short_description='nombre participant'

admin.site.register(Participants)
