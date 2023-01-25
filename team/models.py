from django.db import models
from django.conf import settings



class Team(models.Model):
    name = models.CharField(max_length=100)
    members = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='teams')
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name




