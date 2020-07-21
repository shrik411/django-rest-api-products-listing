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
        prod = Product.objects.get(pk=pk)
        
        if prod:
            categories = prod.categories.all()
            
            json_res = []
            for category in categories:
                category_obj = dict(
                    name = category.name, 
                )
                json_res.append(category_obj)

            return Response(json_res,
                                status=status.HTTP_200_OK)
        else:
            return Response({'status': status.HTTP_404_NOT_FOUND})
