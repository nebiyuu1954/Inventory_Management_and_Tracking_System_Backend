from django.urls import path
from . import views

from .views import ManagerGroupView,SingleManagerGroupView

from .views import InventoryManagementCrewGroupView,SingleInventoryManagementCrewGroupView

from .views import InventoryLogisticsCrewGroupView,SingleInventoryLogisticsCrewGroupView


urlpatterns = [
    
    path('groups/manager/users/', views.ManagerGroupView.as_view()),
    path('groups/manager/users/<int:pk>/', views.SingleManagerGroupView.as_view()),
    
    path('groups/inventory-management-crew/users/', views.InventoryManagementCrewGroupView.as_view()),
    path('groups/inventory-management-crew/users/<int:pk>/', views.SingleInventoryManagementCrewGroupView.as_view()),
    
    path('groups/inventory-logistics-crew/users/', views.InventoryLogisticsCrewGroupView.as_view()),
    path('groups/inventory-logistics-crew/users/<int:pk>/', views.SingleInventoryLogisticsCrewGroupView.as_view()),    

    ]
