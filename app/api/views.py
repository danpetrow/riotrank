from rest_framework import mixins
from rest_framework import generics
from api.models import Team
from api.serializers import TeamSerializer
from django.contrib.auth.models import User
from api.serializers import UserSerializer
from rest_framework import permissions
from api.permissions import IsOwnerOrReadOnly



class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class TeamList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class TeamDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]
    queryset = Team.objects.all()
    serializer_class = TeamSerializer