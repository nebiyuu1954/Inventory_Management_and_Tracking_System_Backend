from django.shortcuts import render


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import Group
from django.contrib.auth.models import User

# Create your views here.
class ManagerGroupView(APIView):
    permission_classes = [IsAuthenticated]
    # throttle_classes = [AnonRateThrottle, UserRateThrottle]
    
    def get(self, request):
        if request.user.is_superuser or request.user.groups.filter(name = 'Manager Group').exists():
            managers_group = Group.objects.get(name='Manager Group')
            managers = managers_group.user_set.all()
            manager_data = [{'id': user.id, 'username': user.username, 'email': user.email} for user in managers]
            return Response(manager_data, status=status.HTTP_200_OK)
        return Response({"detail": "Permission denied"}, status=status.HTTP_403_FORBIDDEN)

    def post(self, request):        
        if request.user.is_superuser or request.user.groups.filter(name = 'Manager Group').exists():
            user_id = request.data.get('user_id')
            if not user_id:
                return Response({"detail": "user ID is required."}, status=status.HTTP_400_BAD_REQUEST)

            try:
                user = User.objects.get(id=user_id)
                managers_group, _ = Group.objects.get_or_create(name='Manager Group')
                
                if user in managers_group.user_set.all():
                    return Response({"detail": "user is already in the manager group."}, status=status.HTTP_400_BAD_REQUEST)
                
                managers_group.user_set.add(user)
                return Response({"detail": "user added to manager group."}, status=status.HTTP_201_CREATED)
            except User.DoesNotExist:
                return Response({"detail": "user not found."}, status=status.HTTP_404_NOT_FOUND)
        return Response({"detail": "Permission denied"}, status=status.HTTP_403_FORBIDDEN)

# class SingleManagerGroupView(APIView):
#     permission_classes = [IsAuthenticated]
#     throttle_classes = [AnonRateThrottle, UserRateThrottle]

#     def delete(self, request, pk):
#         if request.user.is_superuser or request.user.groups.filter(name = 'Manager').exists():  
#             user_id=pk          
#             if not user_id:
#                 return Response({"detail": "user ID is required."}, status=status.HTTP_400_BAD_REQUEST)

#             try:
#                 user = User.objects.get(id=user_id)
#                 managers_group = Group.objects.get(name='Manager')
                
#                 if user not in managers_group.user_set.all():
#                     return Response({"detail": "user is not in the manager group."}, status=status.HTTP_400_BAD_REQUEST)
                
#                 managers_group.user_set.remove(user)
#                 return Response({"detail": "user removed from manager group."}, status=status.HTTP_200_OK)
#             except User.DoesNotExist:
#                 return Response({"detail": "user not found."}, status=status.HTTP_404_NOT_FOUND)
#             except Group.DoesNotExist:
#                 return Response({"detail": "manager group not found."}, status=status.HTTP_404_NOT_FOUND)
#         return Response({"detail": "Permission denied"}, status=status.HTTP_403_FORBIDDEN)



# class DeliveryCrewGroupView(APIView):
#     permission_classes = [IsAuthenticated]
#     throttle_classes = [AnonRateThrottle, UserRateThrottle]
    
#     def get(self, request):
#         if request.user.groups.filter(name = 'Delivery Crew').exists():
#             delivery_crew_group = Group.objects.get(name='Delivery Crew')
#             delivery_crew = delivery_crew_group.user_set.all()
#             delivery_crew_data = [{'id': user.id, 'username': user.username, 'email': user.email} for user in delivery_crew]
#             return Response(delivery_crew_data, status=status.HTTP_200_OK)
#         return Response({"detail": "Permission denied"}, status=status.HTTP_403_FORBIDDEN)

#     def post(self, request):        
#         if request.user.groups.filter(name = 'Delivery Crew').exists():
#             user_id = request.data.get('user_id')

#             try:
#                 user = User.objects.get(id=user_id)
#                 delivery_crew_group, _ = Group.objects.get_or_create(name='Delivery Crew')
                
#                 if user in delivery_crew_group.user_set.all():
#                     return Response({"detail": "user is already in the delivery crew group."}, status=status.HTTP_400_BAD_REQUEST)
                
#                 delivery_crew_group.user_set.add(user)
#                 return Response({"detail": "user added to manager group."}, status=status.HTTP_201_CREATED)
#             except User.DoesNotExist:
#                 return Response({"detail": "user not found."}, status=status.HTTP_404_NOT_FOUND)
#         return Response({"detail": "Permission denied"}, status=status.HTTP_403_FORBIDDEN)

# class SingleDeliveryCrewGroupView(APIView):
#     permission_classes = [IsAuthenticated]
#     throttle_classes = [AnonRateThrottle, UserRateThrottle]


#     def delete(self, request, pk):
#         if request.user.groups.filter(name = 'Delivery Crew').exists():  
#             user_id=pk          
#             if not user_id:
#                 return Response({"detail": "user ID is required."}, status=status.HTTP_400_BAD_REQUEST)

#             try:
#                 user = User.objects.get(id=user_id)
#                 delivery_crew_group = Group.objects.get(name='Delivery Crew')
                
#                 if user not in delivery_crew_group.user_set.all():
#                     return Response({"detail": "user is not in the delivery crew group."}, status=status.HTTP_400_BAD_REQUEST)
                
#                 delivery_crew_group.user_set.remove(user)
#                 return Response({"detail": "user removed from delivery crew group."}, status=status.HTTP_200_OK)
#             except User.DoesNotExist:
#                 return Response({"detail": "user not found."}, status=status.HTTP_404_NOT_FOUND)
#             except Group.DoesNotExist:
#                 return Response({"detail": "delivery crew group not found."}, status=status.HTTP_404_NOT_FOUND)
#         return Response({"detail": "Permission denied"}, status=status.HTTP_403_FORBIDDEN)

