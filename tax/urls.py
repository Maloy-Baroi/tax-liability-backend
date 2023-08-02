from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('super/admin/', admin.site.urls),
    path('auth/', include('App_auth.urls')),
    path('notification/', include('App_notification.urls')),
    path('tax/calculate/', include('App_tax_calculate.urls')),
    path('tax/inspector/', include('App_tax_inspector.urls')),
    path('tax/payer/', include('App_tax_payer.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
