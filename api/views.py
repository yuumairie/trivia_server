from django.shortcuts import render

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework import generics
from django.contrib.auth.models import User
from .models import Task,Trivia,Genre
from rest_framework import viewsets
from .serializers import UserSerializer,TaskSerializer,GenreSerializer,TriviaSerializer
from .ownpermissions import ProfilePermission

class UserViewSet(viewsets.ModelViewSet):
  queryset = User.objects.all()
  serializer_class = UserSerializer
  permission_classes = (ProfilePermission,)

class ManageUserView(generics.RetrieveUpdateAPIView):
  serializer_class = UserSerializer
  authentication_classes = (TokenAuthentication,)
  permission_classes = (IsAuthenticated,)

  def get_object(self):
    return self.request.user

class TaskViewSet(viewsets.ModelViewSet):
  queryset = Task.objects.all()
  serializer_class = TaskSerializer
  authentication_classes = (TokenAuthentication,)
  permission_classes = (IsAuthenticated,)

class GenreViewSet(viewsets.ModelViewSet):
  queryset = Genre.objects.all()
  serializer_class = GenreSerializer
  authentication_classes = (TokenAuthentication,)
  permission_classes = (IsAuthenticated,)

class TriviaViewSet(viewsets.ModelViewSet):
  queryset = Trivia.objects.all()
  serializer_class = TriviaSerializer
  authentication_classes = (TokenAuthentication,)
  permission_classes = (IsAuthenticated,)