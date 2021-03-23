"""tiger URL Configuration

"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from config import admin_site1



urlpatterns = [
    # path('admin/', admin.site.urls),
    path( "abchina-admin/", admin_site1.urls ),
    path('', include( "banking.urls") )

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

