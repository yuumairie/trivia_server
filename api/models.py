from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
  title = models.CharField(max_length=50)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.title

class Genre(models.Model):
  name = models.CharField(max_length=25)
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.name

class Trivia(models.Model):
  user = models.ForeignKey(User,on_delete=models.CASCADE)
  genre = models.ForeignKey(Genre,on_delete=models.CASCADE)
  content = models.TextField(max_length=255)
  good_count = models.IntegerField(default=0)
  created_at = models.DateTimeField(auto_now_add=True)