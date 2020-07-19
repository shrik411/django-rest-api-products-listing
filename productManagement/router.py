from product.viewsets import ProductViewset
from category.viewsets import CategoryViewset
from rest_framework import routers

router = routers.DefaultRouter()

router.register('product', ProductViewset)
router.register('category', CategoryViewset)