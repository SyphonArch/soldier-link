from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('send-check/<message_pk>', views.send_check, name='send-check'),
]
