from django.contrib import admin
from django.contrib.auth import views as auth_views
from mainevent import views as user_views
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path('', include('django.contrib.auth.urls')),
]
if settings.DEBUG: 
	urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT )