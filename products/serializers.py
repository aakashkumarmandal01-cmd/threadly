from rest_framework import serializers
from .models import Product, ProductImage, ProductVariant
class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProductImage; fields=['image','alt_text','sort_order']
class ProductVariantSerializer(serializers.ModelSerializer):
    size=serializers.StringRelatedField(); color=serializers.StringRelatedField()
    class Meta:
        model=ProductVariant; fields=['sku','size','color','stock','available_stock']
class ProductSerializer(serializers.ModelSerializer):
    images=ProductImageSerializer(many=True,read_only=True)
    variants=ProductVariantSerializer(many=True,read_only=True)
    discount_percent=serializers.ReadOnlyField(); average_rating=serializers.ReadOnlyField()
    class Meta:
        model=Product
        fields=['id','name','sku','brand','category','short_description','description','original_price','selling_price','discount_percent','average_rating','images','variants']
