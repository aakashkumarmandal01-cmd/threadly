from django.conf import settings
from django.db import models
from products.models import Product
class RecentlyViewed(models.Model): user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE); product=models.ForeignKey(Product,on_delete=models.CASCADE); viewed_at=models.DateTimeField(auto_now=True)
class SearchHistory(models.Model): user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE); query=models.CharField(max_length=200); created_at=models.DateTimeField(auto_now_add=True)
