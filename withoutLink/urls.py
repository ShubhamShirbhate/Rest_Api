from django.urls import path, include
from rest_framework import routers
from . import views
from .views import MusicianListCreateView, AlbumListCreateView, musicianView,PlaceListCreateView

router = routers.DefaultRouter()
router.register('withoutlink',views.musicianView)

urlpatterns = [
    path('',include(router.urls)),
    path('musician/',views.MusicianListCreateView.as_view()),
    path('album/',views.AlbumListCreateView.as_view()),
    path('place/',views.PlaceListCreateView.as_view())
]
