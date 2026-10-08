from django.contrib import admin
from .models import *
class ImageInline(admin.TabularInline): model=ProductImage; extra=1
class VariantInline(admin.TabularInline): model=ProductVariant; extra=1
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin): list_display=('name','sku','selling_price','is_published','created_at'); list_filter=('is_published','category','gender'); search_fields=('name','sku','brand__name'); inlines=[ImageInline,VariantInline]
admin.site.register([Category,Brand,Size,Color])
