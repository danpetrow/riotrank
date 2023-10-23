from rest_framework import serializers
from api.models import Team, Tournament
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    teams = serializers.PrimaryKeyRelatedField(many=True, queryset=Team.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'team_id']


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        owner = serializers.ReadOnlyField(source='owner.username')
        fields = ['team_id', 'team_code', 'team_name', 'rank']

class GlobalRankingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['team_id', 'team_code', 'team_name', 'rank']

class TournamentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tournament
        owner = serializers.ReadOnlyField(source='owner.username')
        fields = ['tournament_id', 'tournament_name']   

class TeamRankingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['team_id', 'team_code', 'team_name', 'rank']

class TournamentRankingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['team_id', 'team_code', 'team_name', 'rank']

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['team_id', 'team_code', 'team_name', 'rank']
