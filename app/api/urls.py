from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'global_rankings', views.GlobalRankingsViewSet,basename="global_rankings")
router.register(r'teams', views.TeamViewSet,basename="team")
router.register(r'tournaments', views.TournamentViewSet, basename="tournament")
router.register(r'team_rankings',views.TeamRankingsViewSet,basename="team_rankings")
router.register(r'tournament_rankings',views.TournamentRankingsViewSet,basename="tournament_rankings")
router.register(r'games',views.GameViewSet,basename="game")
router.register(r'users',views.UserViewSet,basename="user")


urlpatterns = [
     path('', include(router.urls))
]