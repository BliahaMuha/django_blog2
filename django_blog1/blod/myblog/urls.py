from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import MainView
from django.conf.urls import include
urlpatterns = [
    path('',MainView.as_view(), name='index')
]
