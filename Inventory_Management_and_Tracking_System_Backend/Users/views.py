from django.shortcuts import render

from django.contrib.auth.models import User, Group
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from rest_framework.throttling import UserRateThrottle


class CustomThrottle(UserRateThrottle):
    rate = '10/min'


class BaseGroupView(APIView):
    permission_classes = [IsAuthenticated]
    
    throttle_classes = [CustomThrottle]


    def get_group(self):
        try:
            return Group.objects.get(name=self.group_name)
        except Group.DoesNotExist:
            Response({"detail": f"Group '{self.group_name}' does not exist."}, status=status.HTTP_404_NOT_FOUND)

    def get(self, request):
        if request.user.is_superuser or request.user.groups.filter(name=self.group_name).exists():
            group = self.get_group()
            users = group.user_set.all()
            user_data = [{'id': user.id, 'username': user.username, 'email': user.email} for user in users]
            return Response(user_data, status=status.HTTP_200_OK)
        return Response({"detail": f"Permission denied to access '{self.group_name}' group."}, status=status.HTTP_403_FORBIDDEN)

    def post(self, request):
        if request.user.is_superuser or request.user.groups.filter(name=self.group_name).exists():
            
            user_id = request.data.get('user_id')
            
            if not user_id:
                return Response({"detail": f"User ID is required to access {self.group_name} group."}, status=status.HTTP_400_BAD_REQUEST)

            try:
                user = User.objects.get(id=user_id)
                group, _ = Group.objects.get_or_create(name=self.group_name)

                if user in group.user_set.all():
                    return Response({"detail": f"User is already in the '{self.group_name}' group."}, status=status.HTTP_400_BAD_REQUEST)
                
                user_groups = list(user.groups.values_list('name', flat=True))
                
                for user_group in user_groups:
                    if user_group in {"Manager Crew", "Inventory Management Crew", "Inventory Logistics Crew"} and user_group != self.group_name:
                        return Response({"detail": f"User already belongs to '{user_group}' and cannot be added to '{self.group_name}'."}, status=status.HTTP_400_BAD_REQUEST)

                group.user_set.add(user)
                return Response({"detail": f"User added to '{self.group_name}' group."}, status=status.HTTP_201_CREATED)
            except User.DoesNotExist:
               return Response({"detail":  "User is not found or has not been registered."}, status=status.HTTP_404_NOT_FOUND)
        
        return Response({"detail": f"Permission denied to access '{self.group_name}' group."}, status=status.HTTP_403_FORBIDDEN)


class BaseGroupDeleteView(APIView):
    permission_classes = [IsAuthenticated]
    throttle_classes = [CustomThrottle]

    def get_group(self):
        try:
            return Group.objects.get(name=self.group_name)
        except Group.DoesNotExist:
            raise Http404(f"Group '{self.group_name}' does not exist.")

    def delete(self, request, pk):
        if request.user.is_superuser or request.user.groups.filter(name=self.group_name).exists():
            
            user_id = pk

            try:
                user = User.objects.get(id=user_id)
                group = self.get_group()

                if user not in group.user_set.all():
                    return Response({"detail": f"User is not in the '{self.group_name}' group."}, status=status.HTTP_400_BAD_REQUEST)

                group.user_set.remove(user)
                return Response({"detail": f"User removed from the '{self.group_name}' group."}, status=status.HTTP_200_OK)
            except User.DoesNotExist:
               return Response({"detail": "User is not found or has not been registered."}, status=status.HTTP_404_NOT_FOUND)
        return Response({"detail": f"Permission denied to access '{self.group_name}' group."}, status=status.HTTP_403_FORBIDDEN)


class ManagerGroupView(BaseGroupView):
    group_name = "Manager Crew"

class SingleManagerGroupView(BaseGroupDeleteView):
    group_name = "Manager Crew"

class InventoryManagementCrewGroupView(BaseGroupView):
    group_name = "Inventory Management Crew"

class SingleInventoryManagementCrewGroupView(BaseGroupDeleteView):
    group_name = "Inventory Management Crew"

class InventoryLogisticsCrewGroupView(BaseGroupView):
    group_name = "Inventory Logistics Crew"

class SingleInventoryLogisticsCrewGroupView(BaseGroupDeleteView):
    group_name = "Inventory Logistics Crew"
