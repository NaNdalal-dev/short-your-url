from django.urls import path,include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.conf.urls.static import static
from django.conf import settings
from django.views.static import serve
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path, include
from .views import*
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home)
]

urlpatterns += staticfiles_urlpatterns()