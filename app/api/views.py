from api.models import Team
from api.serializers import TeamSerializer
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
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    
    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        team = self.get_object()
        return Response(team.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)