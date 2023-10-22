from rest_framework import serializers
from api.models import Team
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    teams = serializers.PrimaryKeyRelatedField(many=True, queryset=Team.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'teams']


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        owner = serializers.ReadOnlyField(source='owner.username')
        fields = ['team_id', 'team_code', 'team_name', 'rank']