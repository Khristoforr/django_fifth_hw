from rest_framework.viewsets import ModelViewSet
from .serializers import MeasurementModelSerializer, ProjectModelSerializer
from .models import Project, Measurement


class ProjectViewSet(ModelViewSet):
    """ViewSet для проекта."""
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer


class MeasurementViewSet(ModelViewSet):
    """ViewSet для измерения."""
    queryset = Measurement.objects.all()
    serializer_class = MeasurementModelSerializer
