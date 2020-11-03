from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('genres',views.GenreViewSet)
router.register('trivias',views.TriviaViewSet)
router.register('profile',views.ProfileViewSet)
router.register('commnet',views.CommentViewSet)

urlpatterns = [
    path('',include(router.urls)),
    path('register/',views.CreateUserView.as_view(),name='register'),
    path('myprofile/',views.MyProfileListView.as_view(),name='myprofile'),
]