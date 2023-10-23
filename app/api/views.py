from api.models import Team, Tournament
from api.serializers import TeamSerializer, GlobalRankingsSerializer, TournamentSerializer, TournamentRankingsSerializer
from django.contrib.auth.models import User
from api.serializers import UserSerializer
from rest_framework import permissions
from api.permissions import IsOwnerOrReadOnly
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import renderers



class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class TeamViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]
    queryset = Team.objects.all().order_by('rank')
    serializer_class = TeamSerializer
    
    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    #def highlight(self, request, *args, **kwargs):
    #    team = self.get_object()
    #    return Response(team.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class TournamentViewSet(viewsets.ModelViewSet):
    """
    Returns a list of game_id, and team_id
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]
    serializer_class = TournamentSerializer

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    #def highlight(self, request, *args, **kwargs):
    #    team = self.get_object()
    #    return Response(team.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


    def get_queryset(self):
        """
        """
        queryset = Tournament.objects.all()
        return queryset


class GlobalRankingsViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Returns current top X teams globally
    Returns a list of the top 20 ranked teams by default.

    Accepts a query parameter called number_of_teams to override the number of teams returned.

    [ref]: /riotrank/global_rankings/?number_of_teams=30
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]
    serializer_class = GlobalRankingsSerializer


    def get_queryset(self):
        """
        """
        queryset = Team.objects.all().filter(rank__lte=20).order_by('rank')
        number_of_teams = self.request.query_params.get('number_of_teams')
        if number_of_teams is not None:
            queryset = Team.objects.all().filter(rank__lte=number_of_teams).order_by('rank')
        return queryset

class TeamRankingsViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Returns tournament_rankings from a given list of teams
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]
    serializer_class = GlobalRankingsSerializer


    def get_queryset(self):
        """
        """
        queryset = Team.objects.all().filter(rank__lte=20)
        team_ids = self.request.query_params.get('team_ids')
        if team_ids is not None:
            queryset = Team.objects.all().filter(rank__lte=team_ids)
        return queryset

class TournamentRankingsViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Returns rankings given a tournament_id

    Optional: stage; Returns rankings for a specific stage given a tournament_id

    [ref]: /riotrank/global_rankings/?number_of_teams=30
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]
    serializer_class = GlobalRankingsSerializer


    def get_queryset(self):
        """
        """
        queryset = Team.objects.all().filter(rank__lte=20)
        number_of_teams = self.request.query_params.get('number_of_teams')
        if number_of_teams is not None:
            queryset = Team.objects.all().filter(rank__lte=number_of_teams)
        return queryset

class GameViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Returns a list of game_id, and team_id
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]
    serializer_class = GlobalRankingsSerializer


    def get_queryset(self):
        """
        """
        queryset = Team.objects.all().filter(rank__lte=20)
        number_of_teams = self.request.query_params.get('number_of_teams')
        if number_of_teams is not None:
            queryset = Team.objects.all().filter(rank__lte=number_of_teams)
        return queryset
