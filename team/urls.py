from django.urls import path
from rest_framework import routers
from .views import TeamViewSet


router = routers.DefaultRouter()
router.register('team', TeamViewSet)

urlpatterns = [
    
]

urlpatterns += router.urls
