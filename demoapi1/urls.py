from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('api.urls')),
    path('api/',include('manytomany.urls')),
    path('api2/', include('relations.urls')),
    path('api3/', include('manytoone.urls')),
    path('api4/', include('onetoone.urls')),
    path('api5/', include('manyone1.urls')),
    path('api6/', include('withoutLink.urls'))
]
