from django.db import models

class User(models.Model):
    id = models.CharField(primary_key=True, max_length=18, editable=True, unique=True, default=1)
    username = models.CharField(max_length=100, blank=True, default='')
    team_id = models.ForeignKey('api.Team', related_name='+', on_delete=models.CASCADE)
    tournament_id = models.ForeignKey('api.Tournament', related_name='+', on_delete=models.CASCADE)

class Team(models.Model):
    team_id = models.CharField(primary_key=True, max_length=18, editable=True, unique=True, default=1)
    created = models.DateTimeField(auto_now_add=True)
    team_code = models.CharField(max_length=100, blank=True, default='')
    team_name = models.CharField(max_length=100, blank=True, default='')
    rank = models.IntegerField(default=777)
    owner = models.ForeignKey('auth.User', related_name='api', on_delete=models.CASCADE)

    class Meta:
        ordering = ['created']

class Tournament(models.Model):
    tournament_id = models.CharField(primary_key=True, max_length=100, editable=True, unique=True, default=1)
    tournament_name = models.CharField(max_length=100, blank=True, default='')
    owner = models.ForeignKey('auth.User', related_name='tournament_owner', on_delete=models.CASCADE)


class TournamentRanking(models.Model):
    tournament_ranking_id = models.CharField(primary_key=True, max_length=100, editable=True, unique=True, default=1)
    stage = models.CharField(max_length=100, blank=True, default='')
    tournament_rank = models.IntegerField(default=777)
    tournament_id = models.ForeignKey('api.Tournament', related_name='+', on_delete=models.CASCADE)
    team_id = models.ForeignKey('api.Team', related_name='+', on_delete=models.CASCADE)

class TeamRanking(models.Model):
    team_ranking_id = models.CharField(primary_key=True, max_length=100, editable=True, unique=True, default=1)
    tournament_rank = models.IntegerField(default=777)
    tournament_id = models.ForeignKey('api.Tournament', related_name='+', on_delete=models.CASCADE)
    team_id = models.ForeignKey('api.Team', related_name='+', on_delete=models.CASCADE)

class Game(models.Model):
    game_id = models.CharField(primary_key=True, max_length=100, editable=True, unique=True, default=1)
    team_id = models.ForeignKey('api.Team', related_name='+', on_delete=models.CASCADE)