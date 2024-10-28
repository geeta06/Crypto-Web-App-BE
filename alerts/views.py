from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.decorators import action
from alerts.models import Alert
from alerts.serializers import AlertSerializer


class AlertViewSet(viewsets.ModelViewSet):
    
    queryset = Alert.objects.all()
    serializer_class = AlertSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=False, methods=['get'])
    def my_alerts(self, request):
        alerts = Alert.objects.filter(user=request.user)
        serializer = self.get_serializer(alerts, many=True)
        return Response(serializer.data)
