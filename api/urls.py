from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.index),
    #path('',views.ListView.as_view()),
    path('List',views.ListCreateView.as_view()),
    path('list/<int:pk>',views.RetrieveUpdateDestroy.as_view()),
    #path('update/<int:pk>',views.UpdateView.as_view()),
    path('list/',views.List),
    path('create/', views.Create),
    path('details/<int:pk>', views.Details),
]
