from rest_framework import status, viewsets
from .models import Category
from . import serializers
from rest_framework.decorators import action
from rest_framework.response import Response
from django.forms.models import model_to_dict


class CategoryViewset(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer

    @action(methods=['get'], detail=True)
    def product(self, request, pk=None):
        selectedCategory = Category.objects.get(pk=pk)
        
        if selectedCategory:
            products = selectedCategory.product_set.all()
            
            json_res = []
            for product in products:
                product_obj = dict(
                    name = product.name, 
                )
                json_res.append(product_obj)

            return Response(json_res,
                                status=status.HTTP_200_OK)
        else:
            return Response({'status': status.HTTP_404_NOT_FOUND})

