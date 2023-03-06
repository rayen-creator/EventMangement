from django.urls import path
from .views import *
urlpatterns = [
    # path('<str:name>', index),
    # path('list/',list_event),
    path('', ListEvents.as_view(), name="Affiche"),
    path('add/', AddEv, name="add"),
    path('update/<int:pk>', UpdateEvent.as_view(), name="update"),
    path('delete/<int:pk>', DeleteEvent.as_view(), name="delete"),
    path('details/<int:pk>', detailsss, name="details"),
    path('participer/<int:event_id>', participer, name="participer"),



]
