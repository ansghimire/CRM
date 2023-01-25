from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework.mixins import CreateModelMixin
from rest_framework import permissions
from rest_framework.response import Response

from .models import Client, Note
from team.models import Team
from .serializers import ClientSerializer, NoteSerializer




class ClientViewSet(ModelViewSet):
    queryset = Client.objects.select_related('created_by').select_related('team').all()
    serializer_class = ClientSerializer


    def get_queryset(self):
        team = Team.objects.filter(members__in=[self.request.user]).first()
        qs = self.queryset.filter(team=team)
        return qs   

    def perform_create(self, serializer):
        team = Team.objects.filter(members__in=[self.request.user]).first()
        return serializer.save(created_by=self.request.user, team=team)


class NoteViewSet(GenericViewSet, CreateModelMixin):
    queryset = Note.objects.select_related('team').select_related('created_by').all()
    serializer_class = NoteSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


    def perform_create(self, serializer):
        team = Team.objects.filter(members__in=[self.request.user]).first()
        return serializer.save(team = team, created_by=self.request.user)


class NoteForClientAPIView(APIView):
    serializer_class = NoteSerializer
    # permission_classes = [permissions.AllowAny]
    queryset = Note.objects.select_related('created_by').select_related('team').all()

    def get(self, request, pk=None, *args, **kwargs):
        client = get_object_or_404(Client, pk=pk)
        note = self.queryset.filter(client = client)
        serializer = NoteSerializer(note, many=True)   
        return Response(serializer.data)


class NoteForClientUpdateRetrieveAPIView(APIView):
    serializer_class = NoteSerializer
    # permission_classes = [permissions.AllowAny]
    queryset = Note.objects.select_related('created_by').select_related('team').all()

    def get_object(self, pk, id):
        try:
            return Note.objects.get(client=pk, id=id)
        except Note.DoesNotExist:
            raise Http404


    def get(self, request, pk=None, id=None, *args, **kwargs):
        
        note = self.get_object(pk, id)
        serializer = self.serializer_class(note)
        return Response(serializer.data)
    
    def put(self, request, pk, id, format=None, *args, **kwargs):
        note = self.get_object(pk, id)

        request.data['client'] = id

        serializer = self.serializer_class(instance=note, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
        

    
    
    
  


    
    