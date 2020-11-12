from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework import generics
from .models import Trivia,Genre,Profile,Comment
from rest_framework import viewsets
from . import serializers
from .ownpermissions import ProfilePermission


class CreateUserView(generics.CreateAPIView):
  serializer_class = serializers.UserSerializer
  permission_classes = (AllowAny,)

class ProfileViewSet(viewsets.ModelViewSet):
  permission_classes = (ProfilePermission,)
  queryset = Profile.objects.all()
  serializer_class = serializers.ProfileSerializer
  
  def perform_create(self,selializer):
    selializer.save(userProfile=self.request.user)

class MyProfileListView(generics.ListAPIView):
  queryset = Profile.objects.all()
  serializer_class = serializers.ProfileSerializer
  def get_queryset(self):
    return self.queryset.filter(userProfile=self.request.user)

class GenreViewSet(viewsets.ModelViewSet):
  queryset = Genre.objects.all()
  serializer_class = serializers.GenreSerializer
  permission_classes = (AllowAny,)

class TriviaViewSet(viewsets.ModelViewSet):
  permission_classes = (ProfilePermission,)
  queryset = Trivia.objects.all()
  serializer_class = serializers.TriviaSerializer

  def perform_create(self,serializer):
    serializer.save(userPost=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
  queryset = Comment.objects.all()
  serializer_class = serializers.CommentSerializer

  def perform_create(self,selializer):
    serializer.save(userComment=self.request.user)