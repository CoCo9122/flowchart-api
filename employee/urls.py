from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import get_active_user, get_active_flowchart, update_active_flowchart, insert_edge

urlpatterns = [
    path('getActiveUser/', get_active_user),
    path('getActiveFlowChart/<int:id>', get_active_flowchart),
    path('updateActiveFlowChart/<int:id>', update_active_flowchart),
    path('insertFlowChart', insert_edge)
]