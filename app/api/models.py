from django.db import models

class Team(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    team_name = models.CharField(max_length=100, blank=True, default='')

    class Meta:
        ordering = ['created']