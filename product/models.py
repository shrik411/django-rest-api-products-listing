from django.db import models
from category.models import Category 

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    code = models.CharField(max_length=15)
    price = models.FloatField(default=0.00)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.name

# Create/ Insert / Add - {POST}
# Update - {PUT}
# Delete - {DELETE}