from rest_framework.permissions import BasePermission


class IsModerator(BasePermission):

    def has_permission(self, request, view):
        return request.user.groups.filter(name='Moderator').exists()


class IsOwner(BasePermission):

    def has_permission(self, request, view):
        if view.get_object().owner == request.user:
            return True
        return False
