from django.db import models

class Team(models.Model):
    team_id = models.CharField(primary_key=True, max_length=18, editable=True, unique=True, default=1)
    created = models.DateTimeField(auto_now_add=True)
    team_code = models.CharField(max_length=100, blank=True, default='')
    team_name = models.CharField(max_length=100, blank=True, default='')
    rank = models.IntegerField(null=True)
    owner = models.ForeignKey('auth.User', related_name='api', on_delete=models.CASCADE)

    class Meta:
        ordering = ['created']