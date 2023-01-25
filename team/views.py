from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404

from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework.mixins import CreateModelMixin
from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Team
from .serializers import TeamSerializer
from .permissions import TeamOwnerAuthorizedUSer


User = get_user_model()

### team owner can delete, update, 
class TeamViewSet(ModelViewSet):
    queryset = Team.objects.select_related('created_by').prefetch_related('members').all()
    serializer_class = TeamSerializer
   
    
    def get_queryset(self):
        if self.request.user.is_superuser:
            return self.queryset
        return self.queryset.filter(members__in=[self.request.user])
    
    def get_permissions(self):
        if self.action == 'list':
            return [permissions.IsAuthenticated()]
        elif self.action == 'retrieve':
            return [permissions.IsAuthenticated()]
        elif self.action == 'destroy':
            return [TeamOwnerAuthorizedUSer()]      
        elif self.action == 'partial_update':
            return [TeamOwnerAuthorizedUSer()] 
        elif self.action == 'update':
            return [TeamOwnerAuthorizedUSer()]
        return super().get_permissions()
    
    def perform_create(self, serializer):
        obj = serializer.save(created_by= self.request.user)
        obj.members.add(self.request.user)
        return obj 
    

# only team owner can add members
    @action(detail=True, url_path="create-member", methods=['POST'],  permission_classes=[TeamOwnerAuthorizedUSer])
    def create_member(self, request, pk=None):
        team = self.get_object()
        try:
            email = request.data['email']
        except:
            return Response({"email":"email is required"})
        user = get_object_or_404(User, email=email)
        team.members.add(user)
        return Response({"detail": f'{email} added to the team'})

     
        



    

    




