from django.contrib import admin
from django.urls import path
from myapp.views import form_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', form_view, name='form_view'),
]
