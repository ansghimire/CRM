from django.db import models
from django.contrib.auth import get_user_model
from team.models import Team

User = get_user_model()


class Lead(models.Model):
   
    CHOICES_STATUS = (
        ('new', 'New'),
        ('contacted', 'Contacted'),
        ('inprogress', 'In progress'),
        ('lost', 'Lost'),
        ('won', 'Won'),
    )


    CHOICES_PRIORITY = (
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    )

    team = models.ForeignKey(Team, related_name='leads', on_delete=models.CASCADE)
    company = models.CharField(max_length=255)
    contact_person = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=255)
    website = models.CharField(max_length=255, blank=True, null=True)
    confidence = models.IntegerField(blank=True, null=True)
    estimated_value = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=25, choices=CHOICES_STATUS, default='new')
    priority = models.CharField(max_length=25, choices=CHOICES_PRIORITY, default='medium')
    assigned_to = models.ForeignKey(User, related_name='assignedleads', blank=True, null=True, on_delete=models.SET_NULL)
    created_by = models.ForeignKey(User, related_name='leads', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)