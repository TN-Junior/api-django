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
