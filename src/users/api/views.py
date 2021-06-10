from rest_framework import permissions
from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView

from django.contrib.auth import get_user_model
from django.shortcuts import render, get_object_or_404

from .serializers import UserSerializer, UserProfileSerializer
from users.models import Profile


class CreateUserView(CreateAPIView):

    model = get_user_model()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = UserSerializer


class ProfileView(RetrieveUpdateAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = [
        permissions.IsAuthenticated
    ]

    def get_queryset(self):
        u = get_object_or_404(Profile, user=self.kwargs.get('username'))

        return Profile.objects.get(user=u)
