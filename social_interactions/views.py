from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.db import models
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from rest_framework_simplejwt.tokens import RefreshToken
from .models import FriendRequest
from .serializers import FriendRequestSerializer, FriendRequestActionSerializer
from rest_framework.permissions import IsAuthenticated
from .throttles import FriendRequestThrottle
from  user_management.serializers import CustomUserSerializer
from .pagination import CustomPagination

User = get_user_model()

class UserSearchView(generics.ListAPIView):
    serializer_class = CustomUserSerializer
    pagination_class = CustomPagination  # Use the custom pagination class
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        query = self.request.query_params.get('q', '')
        return User.objects.filter(models.Q(email__icontains=query) | models.Q(name__icontains=query)).distinct()
        
class SendFriendRequestView(APIView):
    permission_classes = [IsAuthenticated]
    throttle_classes = [FriendRequestThrottle]

    def post(self, request, *args, **kwargs):
        to_user_id = request.data.get('to_user_id')
        from_user = request.user

        if not to_user_id:
            return Response({'detail': 'to_user_id is required'}, status=status.HTTP_400_BAD_REQUEST)

        if from_user.id == to_user_id:
            return Response({'detail': 'You cannot send a friend request to yourself'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            to_user = User.objects.get(id=to_user_id)
        except User.DoesNotExist:
            return Response({'detail': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        if FriendRequest.objects.filter(from_user=from_user, to_user=to_user).exists():
            return Response({'detail': 'Friend request already sent'}, status=status.HTTP_400_BAD_REQUEST)

        friend_request = FriendRequest(from_user=from_user, to_user=to_user)
        friend_request.save()
        return Response(FriendRequestSerializer(friend_request).data, status=status.HTTP_201_CREATED)


class HandleFriendRequestView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        friend_request_id = request.data.get('friend_request_id')
        action = request.data.get('action')
        user = request.user

        if not friend_request_id or not action:
            return Response({'detail': 'friend_request_id and action are required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            friend_request = FriendRequest.objects.get(id=friend_request_id, to_user=user)
        except FriendRequest.DoesNotExist:
            return Response({'detail': 'Friend request not found'}, status=status.HTTP_404_NOT_FOUND)

        if action == 'accept':
            friend_request.status = 'accepted'  # Assuming you have a status field
            friend_request.save()
            return Response({'detail': 'Friend request accepted'}, status=status.HTTP_200_OK)
        elif action == 'reject':
            friend_request.status = 'rejected'  # Assuming you have a status field
            friend_request.save()
            return Response({'detail': 'Friend request rejected'}, status=status.HTTP_200_OK)
        else:
            return Response({'detail': 'Invalid action'}, status=status.HTTP_400_BAD_REQUEST)

class ListFriendsView(generics.ListAPIView):
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        friends = FriendRequest.objects.filter(
            (models.Q(from_user=user) | models.Q(to_user=user)),
            status='accepted'
        )
        friend_ids = [fr.to_user.id if fr.from_user == user else fr.from_user.id for fr in friends]
        return User.objects.filter(id__in=friend_ids)


class ListPendingRequestsView(generics.ListAPIView):
    serializer_class = FriendRequestSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return FriendRequest.objects.filter(from_user=self.request.user, status='pending')