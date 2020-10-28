from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('post', views.PostView)
router.register('post-rate', views.PostRatesView)


urlpatterns = [
   path('',include(router.urls))
]
