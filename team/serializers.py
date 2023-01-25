from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Team

User = get_user_model()



class TeamSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField(read_only=True)
    members = serializers.StringRelatedField(many=True, read_only=True)


    class Meta:
        model = Team
        fields = ['id', 'name', 'members', 'created_by', 'created_at']
        read_only_fields = ('id', 'created_at', 'created_by', 'members')


    