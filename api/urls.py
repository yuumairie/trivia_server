from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from .views import TaskViewSet,UserViewSet,ManageUserView,GenreViewSet,TriviaViewSet

router = routers.DefaultRouter()
router.register('tasks',TaskViewSet)
router.register('users',UserViewSet)
router.register('genres',GenreViewSet)
router.register('trivias',TriviaViewSet)

urlpatterns = [
    path('myself/',ManageUserView.as_view(),name='myself'),
    path('',include(router.urls))
]