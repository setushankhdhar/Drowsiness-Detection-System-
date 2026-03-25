from django.urls import path
from . import views

urlpatterns = [
    path('',        views.index,      name='index'),
    path('about/',  views.about,      name='about'),
    path('detect/', views.detect,     name='detect'),
    path('video/',  views.video_feed, name='video_feed'),
    path('status/', views.status,     name='status'),
]
