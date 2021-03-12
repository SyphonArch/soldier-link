from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('send-check/', views.send_check),
]