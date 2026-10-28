from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer
class ProductViewSet(viewsets.ModelViewSet):

    # Full CRUD: list, create, retrieve, update,
    # partial_update, destroy

    queryset = Product.objects.all() 
    serializer_class = ProductSerializer
