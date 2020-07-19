from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Product
from . import serializers
from django.forms.models import model_to_dict


class ProductViewset(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = serializers.ProductSerializer

    @action(methods=['get'], detail=True)
    def category(self, request, pk=None):
        product_data = Product.objects.filter(pk=pk).first()
        
        if product_data:
            data = model_to_dict(product_data)
            return Response(data,
                            status=status.HTTP_200_OK)
        else:
            return Response({'status': status.HTTP_404_NOT_FOUND})
