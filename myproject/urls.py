from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from myapp.views import dashboard_view, form_view

urlpatterns = [
    path('', form_view, name='form_view'),
    path('dashboard/', dashboard_view, name='dashboard'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
