from django.urls import path, include
from rest_framework import routers
from . import views
from .views import CarView

router = routers.DefaultRouter()
router.register('carapi',views.CarView)

urlpatterns = [
    path('',include(router.urls))
]
