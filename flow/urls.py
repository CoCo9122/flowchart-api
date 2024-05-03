from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import get_flow_types, get_edge, get_flow_type, get_node, insert_edge, insert_node, update_edge, update_node

urlpatterns = [
    path('getFlowTypes/', get_flow_types),
    path('getFlowType/<int:id>', get_flow_type),
    path('getEdge/<int:id>', get_edge),
    path('getNode/<int:id>', get_node),
    path('insertNode', insert_node),
    path('insertEdge', insert_edge),
    path('updateNode/<int:id>', update_node),
    path('updateEdge/<int:id>', update_edge),
]