from rest_framework import serializers
from .models import Lead


class LeadSerializer(serializers.ModelSerializer):
    team = serializers.StringRelatedField(read_only=True)
    assigned_to = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Lead
        fields = '__all__'
        read_only_fields = ('created_at','created_by', 'created_at','modified_at','team')