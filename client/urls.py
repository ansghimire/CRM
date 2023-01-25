from django.urls import path
from rest_framework import routers
from .views import (ClientViewSet,NoteViewSet,
                    NoteForClientAPIView,
                    NoteForClientUpdateRetrieveAPIView)


router = routers.DefaultRouter()
router.register('client', ClientViewSet)
router.register('note', NoteViewSet)

urlpatterns = [
    path("client/<int:pk>/note/", NoteForClientAPIView.as_view()),
    path("client/<int:pk>/note/<int:id>/", NoteForClientUpdateRetrieveAPIView.as_view())
]

urlpatterns += router.urls