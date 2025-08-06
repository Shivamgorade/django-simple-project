from django.urls import path
from . import views

urlpatterns = [
    path('', views.form_view, name='form_view'),  # Existing form page
    path('dashboard/', views.dashboard_view, name='dashboard'),  # Renders dashboard.html
    path('api/chart-data/', views.get_filtered_chart_data, name='chart_data'),  # API for chart data
    path('api/chart-data-st20/', views.get_filtered_chart_data_st20, name='chart-data-st20'),
    path('api/chart-data-st25c/', views.get_filtered_chart_data_st25c, name='chart_data_st25c'),
    path('api/chart-data-st25mv/', views.get_filtered_chart_data_st25mv, name='chart_data_st25mv'),
    path('api/chart-data-st30/', views.get_filtered_chart_data_st30, name='chart_data_st30'),
    path('api/chart-data-st40/', views.get_filtered_chart_data_st40, name='chart_data_st40'),
     path("api/info-card-data/", views.info_card_api, name="info_card_api"),
     path('api/total-inspections/', views.total_inspections_api, name='total_inspections'),
     




]
