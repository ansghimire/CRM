from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework import permissions
from rest_framework.response import Response
from team.models import Team
from client.models import Client
from .models import Lead
from .serializers import LeadSerializer
from team.permissions import TeamOwnerAuthorizedUSer
from client.serializers import ClientSerializer


class LeadViewSet(ModelViewSet):
    queryset = Lead.objects.select_related('team').select_related('assigned_to').all()
    serializer_class = LeadSerializer

    def get_queryset(self):
        team = Team.objects.filter(members__in=[self.request.user]).first()
        return Lead.objects.filter(team=team)
    
    def perform_create(self, serializer):
        team = Team.objects.filter(members__in=[self.request.user]).first()        
        return serializer.save(team=team, created_by=self.request.user)


    @action(detail=True, url_path="convert-to-client", methods=['POST'], permission_classes=[TeamOwnerAuthorizedUSer])
    def convert_to_client(self, request, pk=None):
        lead = self.get_object()
        print("============")
        print(lead.company)
        print("=============")

        client = Client.objects.create(
            team = lead.team,
            name = lead.company,
            contact_person = lead.contact_person,
            email = lead.email,
            phone = lead.phone,
            website=lead.website,
            created_by=lead.created_by
        )
        serializer = ClientSerializer(instance=client)
        lead.delete()
        return Response(serializer.data, status=200)





        







