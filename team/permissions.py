from rest_framework import permissions



class TeamOwnerAuthorizedUSer(permissions.BasePermission):
    '''
    Ownly Team owner can update and delete the object
    '''
    def has_object_permission(self, request, view, obj):
        return obj.created_by == request.user or request.user.is_superuser