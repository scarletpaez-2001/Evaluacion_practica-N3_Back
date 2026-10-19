from django.shortcuts import render

from rest_framework import viewsets
from .models import Solicitud
from .serializers import SolicitudSerializer
from .permissions import EsPropietarioOAdministrador

class SolicitudViewSet(viewsets.ModelViewSet):
    serializer_class = SolicitudSerializer
    permission_classes = [EsPropietarioOAdministrador]

    def get_queryset(self):
        user = self.request.user
        # Si es administrador, ve todas las solicitudes. Si es usuario normal, solo ve las suyas.
        if user.is_staff:
            return Solicitud.objects.all().order_by('-fecha_creacion')
        return Solicitud.objects.filter(usuario=user).order_by('-fecha_creacion')

    def perform_create(self, serializer):
        # Asigna automáticamente el usuario autenticado al crear la solicitud
        serializer.save(usuario=self.request.user)

    def perform_update(self, serializer):
        user = self.request.user
        # Si no es staff, asegurar que no modifiquen el estado ni cambien el usuario o la fecha
        if not user.is_staff:
            serializer.save(usuario=self.request.user)
        else:
            serializer.save()
