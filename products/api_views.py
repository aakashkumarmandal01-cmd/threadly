from rest_framework.generics import ListAPIView
from .models import Product
from .serializers import ProductSerializer
class ProductListAPI(ListAPIView): queryset=Product.objects.filter(is_published=True).select_related('brand','category'); serializer_class=ProductSerializer; search_fields=['name','sku','tags','description','brand__name']; ordering_fields=['selling_price','created_at']
