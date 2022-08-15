
from xml.dom.minidom import Document
from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Home, name = 'home'),
    #url aplicaciones
    path('Noticias/', include('apps.noticias.urls')),
    path('Quienes/', include('apps.quienes.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
