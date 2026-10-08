from django.conf import settings
from django.db import models
from products.models import Product
class Review(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name='reviews')
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    rating=models.PositiveSmallIntegerField()
    text=models.TextField()
    image=models.ImageField(upload_to='reviews/',blank=True)
    is_approved=models.BooleanField(default=True)
    created_at=models.DateTimeField(auto_now_add=True)
    class Meta:
        constraints=[models.UniqueConstraint(fields=['product','user'],name='one_review_per_user_product')]
