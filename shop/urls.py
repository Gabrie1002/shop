from django.contrib import admin
from django.urls import path, include
from apps.main import views
from django.conf.urls.static import static
from django.conf import settings
from apps.catalog.urls import urlpatterns as url_catalog

urlpatterns = [
    path('', views.index),
    path('about/', views.about, name='about'),
    path('payments/', views.payments, name='payments'),
    path('delivery/', views.delivery, name='delivery'),
    path('about/mission/', views.mission, name='mission'),
    path('about/contacts/', views.contacts, name='contacts'),
    path('about/requisites/', views.requisites, name='requisites'),
    path('admin/', admin.site.urls),
    path('tinymce/', include('tinymce.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += url_catalog