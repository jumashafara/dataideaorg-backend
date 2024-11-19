from django.urls import path
from . import views

urlpatterns = [
    path(route='activities/', view=views.ActivityView.as_view(), name='activity-create'),
]
