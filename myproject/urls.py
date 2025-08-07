from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from myapp.views import python_version_view

urlpatterns = [
    path('', include('myapp.urls')),  # All routing handled in myapp.urls
     path('python-version/', python_version_view, name='python_version'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
