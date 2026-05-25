from rest_framework import viewsets, filters
from django_filters import rest_framework as django_filters
from .models import Property
from .serializers import PropertySerializer

class PropertyFilter(django_filters.FilterSet):
    min_price = django_filters.NumberFilter(field_name="price", lookup_expr='gte')
    max_price = django_filters.NumberFilter(field_name="price", lookup_expr='lte')
    min_area = django_filters.NumberFilter(field_name="total_area", lookup_expr='gte')
    max_area = django_filters.NumberFilter(field_name="total_area", lookup_expr='lte')

    class Meta:
        model = Property
        fields = {
            'age_status': ['exact'],
            'rooms': ['exact', 'gte'],
            'bedrooms': ['exact', 'gte'],
            'bathrooms': ['exact'],
            'garages': ['exact'],
        }

class PropertyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Property.objects.filter(is_active=True).order_by('-created_at')
    serializer_class = PropertySerializer
    filter_backends = [django_filters.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = PropertyFilter
    search_fields = ['location', 'description']
    ordering_fields = ['price', 'total_area', 'created_at']