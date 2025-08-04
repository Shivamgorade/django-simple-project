from django.urls import path
from . import views

urlpatterns = [
    path('', views.form_view, name='form_view'),  # Existing form page
    path('dashboard/', views.dashboard_view, name='dashboard'),  # Renders dashboard.html
    path('api/chart-data/', views.get_filtered_chart_data, name='chart_data'),  # API for chart data
]
