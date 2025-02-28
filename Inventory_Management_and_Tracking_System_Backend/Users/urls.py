
from django.urls import path
from . import views

from .views import ManagerGroupView


urlpatterns = [
    
    path('groups/manager/users/', views.ManagerGroupView.as_view()),
    # path('groups/manager/users/<int:pk>/', views.SingleManagerGroupView.as_view()),
    
    # path('groups/delivery-crew/users/', views.DeliveryCrewGroupView.as_view()),
    # path('groups/delivery-crew/users/<int:pk>/', views.SingleDeliveryCrewGroupView.as_view()),    

    ]
