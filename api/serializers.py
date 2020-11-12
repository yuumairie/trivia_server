from rest_framework import serializers
from .models import Genre,Trivia,Profile,Comment
from django.contrib.auth import get_user_model
# from rest_framework.authtoken.models import Token

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = get_user_model()
    fields = ('id','email','password')
    extra_kwargs = {'password':{'write_only':True,'required':True}}
  
  def create(self,validated_data):
    user = get_user_model().objects.create_user(**validated_data)
    return user

class ProfileSerializer(serializers.ModelSerializer):
  created_on = serializers.DateTimeField(format="%Y-%m-%d %H:%M",read_only=True)

  class Meta:
    model = Profile
    fields = ('id','nickName','userProfile','created_on','img')
    extra_kwargs = {'userProfile':{'read_only':True}}

class GenreSerializer(serializers.ModelSerializer):
  class Meta:
    model = Genre
    fields = ('id','name')

class TriviaSerializer(serializers.ModelSerializer):
  # userPost = UserSerializer(read_only=True)
  # genre = GenreSerializer(read_only=True)
  created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M",read_only=True)

  class Meta:
    model = Trivia
    fields = ('id','userPost','genre','content','created_at')
    extra_kwargs = {'userPost':{'read_only':True}}

class CommentSerializer(serializers.ModelSerializer):
  class Meta:
    model = Comment
    fields = ('id','text','userComment','post')
    extra_kwargs={'userComment':{'read_only':True}}
