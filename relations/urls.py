from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('languages', views.LanguagesView, base_name='languages')
router.register('paradigm', views.ParadigmView, base_name='paradigm')
router.register("programmers", views.ProggrammerViews)


urlpatterns = [
  path('', include(router.urls))
]
