from rest_framework.viewsets import ModelViewSet
from .serializers import OrderSerializer
from ..models import Order

class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    