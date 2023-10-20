from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = [
    path('teams/', views.team_list),
    path('teams/<int:pk>/', views.team_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)