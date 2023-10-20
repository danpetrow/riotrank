from django.urls import path
from api import views

urlpatterns = [
    path('teams/', views.team_list),
    path('teams/<int:pk>/', views.team_detail),
]