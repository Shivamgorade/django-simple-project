from django.urls import path
from .views import form_view
from myapp import views

urlpatterns = [
    path('', form_view, name='form_view'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
]
