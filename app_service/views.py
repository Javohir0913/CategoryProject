from app_service.models import Service
from app_service.serializers import GetServiceSerializer, ServiceSerializer
from rest_framework import viewsets, permissions


class ServiceViewset(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return GetServiceSerializer
        return ServiceSerializer
