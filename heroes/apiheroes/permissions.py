from rest_framework.permissions import BasePermission



#Permiso personalizado para que solo los administradores puedan hacer POST, PUT y DELETE (este permiso se puede asignar a cualquier vista o app)
class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        else:
            return request.user.is_staff