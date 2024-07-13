from django_filters import rest_framework as filters
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from apps.accessories.models import Accessory
from .serializers import AccessorySerializer


class AccessoryFilter(filters.FilterSet):
    title = filters.CharFilter(field_name='title', lookup_expr='icontains')
    price = filters.NumberFilter(field_name='price', lookup_expr='exact')  # Или используйте `range` для диапазона

    class Meta:
        model = Accessory
        fields = ['title', 'price', 'stock', 'restock_date']  # Добавьте поля, которые вам нужны


class AccessoryViewSet(viewsets.ModelViewSet):
    queryset = Accessory.objects.all()
    serializer_class = AccessorySerializer
    permission_classes = [IsAuthenticated]
    filter_backends = (DjangoFilterBackend,)
    filterset_class = AccessoryFilter
