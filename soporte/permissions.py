from rest_framework import permissions

class EsPropietarioOAdministrador(permissions.BasePermission):
    """
    Permisos
    - Administradores (is_staff): control total (crear, ver todas, editar todo, cambiar estado, eliminar).
    - Usuario normal: para ver y editar solo sus propias solicitudes, pero NO puede cambiar el estado ni eliminar registros.
    """

    def has_permission(self, request, view):
        # Todo usuario autenticado puede listar y crear solicitudes
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        # Si es administrador, tiene acceso total
        if request.user.is_staff:
            return True

        # Si es usuario normal:
        # 1. No puede eliminar registros bajo ningún punto de vista por la API
        if request.method == 'DELETE':
            return False

        # 2. Solo puede acceder si el objeto le pertenece
        if obj.usuario != request.user:
            return False

        # 3. Si intenta modificar datos (PUT o PATCH), validar restricciones de campos
        if request.method in ['PUT', 'PATCH']:
            # Validar si se intenta cambiar el estado y el usuario no es staff
            if 'estado' in request.data and request.data['estado'] != obj.estado:
                return False

        return True