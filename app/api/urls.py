from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'teams', views.TeamViewSet,basename="team")
router.register(r'users',views.UserViewSet,basename="user")

urlpatterns = [
     path('', include(router.urls))
]