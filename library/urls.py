from django.urls import path, include
from .import views

app_name = 'library'

urlpatterns = [
    path('resources/', views.ResourcesView.as_view(), name='resources'),
    path('resources/<int:id>/', views.ResourceDetailView.as_view(), name='resource-detail'),
    path('download/<int:resource_id>/', views.DownloadResourceView.as_view(), name='download_resource'),
]