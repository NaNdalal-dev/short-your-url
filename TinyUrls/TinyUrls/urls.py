from django.contrib import admin
from django.urls import path
from .views import*
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home)
]

urlpatterns += staticfiles_urlpatterns()