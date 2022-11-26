from django.urls import path

from .views import MainView
from django.conf.urls import include
urlpatterns = [
    path('',MainView.as_view(), name='index')
]