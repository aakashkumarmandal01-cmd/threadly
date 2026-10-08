from django.db import models
from products.models import ProductVariant
class StockMovement(models.Model): variant=models.ForeignKey(ProductVariant,on_delete=models.CASCADE,related_name='movements'); change=models.IntegerField(); reason=models.CharField(max_length=100); created_at=models.DateTimeField(auto_now_add=True)
