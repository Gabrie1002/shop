from django.contrib import admin
from django.urls import path
from apps.main import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.index),
    path('about/', views.about, name='about'),
    path('about/mission/', views.mission, name='mission'),
    path('admin/', admin.site.urls),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
