from django.urls import path
from .views import index, list_event
urlpatterns = [
    path('<str:name>', index),
    path('list/',list_event)
]