from django.urls.conf import path
from django.urls import path, include
from rest_framework import routers
from .views import ( 
    CreateUserView, ListUserView, LoginUserView,
    ProfileViewSet, CategoryViewSet, TaskViewSet
)

router = routers.DefaultRouter()
router.register('profile', ProfileViewSet)
router.register('category', CategoryViewSet)
router.register('tasks', TaskViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('create/', CreateUserView.as_view(), name='create'),
    path('users/', ListUserView.as_view(), name="users"),
    path('loginuser/', LoginUserView.as_view(), name="loginuser"),
]