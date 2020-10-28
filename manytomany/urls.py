from django.urls import path, include
from .views import StudentViewSet, ModulViewSet
from rest_framework import routers
#from rest_framework.routers import DefaultRouter

router = routers.DefaultRouter()
router.register('student', StudentViewSet, base_name = "student")
router.register('module', ModulViewSet, base_name = "module")


urlpatterns = [
    path('',include(router.urls))
    #path('',views.StudentView.as_view()),
    #path('details/<int:pk>/',views.details),
    #path('module/',views.ModulView.as_view()),
    #path('create/', views.create),
]
