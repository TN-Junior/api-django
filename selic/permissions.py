from rest_framework import permissions

class ReadOnlyOrAuthenticated(permissions.BasePermission):
    """
    Permite acesso irrestrito para leitura (GET),
    mas exige autenticação para métodos de escrita (POST, PUT, DELETE).
    """
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:  # GET, HEAD, OPTIONS não exigem token
            return True
        return request.user and request.user.is_authenticated  # Apenas autenticados podem modificar

    def has_object_permission(self, request, view, obj):
        """Restringe DELETE apenas para superusuários"""
        if request.method == "DELETE":
            return request.user.is_superuser  # Apenas superusuários podem deletar
        return True