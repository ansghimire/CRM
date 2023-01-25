from django.urls import path 
from rest_framework import routers
from .views import LeadViewSet


router = routers.DefaultRouter()
router.register('lead', LeadViewSet)


urlpatterns = [
    
]
urlpatterns += router.urls
