from rest_framework import serializers
from .models import Client, Note



class ClientSerializer(serializers.ModelSerializer):
    team = serializers.StringRelatedField()
    created_by = serializers.StringRelatedField()


    class Meta:
        model = Client
        fields = ['id', 'team', 'name', 'contact_person', 'email', 'phone',
                 'website', 'created_by', 'created_at', 'modified_at' ]
        read_only_fields = ('id', 'team', 'created_by',  'created_at', 'modified_at')


class NoteSerializer(serializers.ModelSerializer):
    team = serializers.StringRelatedField(read_only=True)
    created_by = serializers.StringRelatedField(read_only=True)
    # client = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model = Note
        fields = ['id', 'team', 'client', 'name', 'body', 'created_by', 'created_at', 'modified_at']
        read_only_fields = ('id', 'team', 'created_by', 'created_at', 'modified_at')

