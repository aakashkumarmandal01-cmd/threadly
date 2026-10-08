from django.contrib import admin
from .models import Order,OrderItem,Payment
class ItemInline(admin.TabularInline): model=OrderItem; extra=0; readonly_fields=('product_name','unit_price','quantity','size','color')
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin): list_display=('order_id','user','status','payment_status','total','created_at'); list_filter=('status','payment_status'); search_fields=('order_id','user__email'); inlines=[ItemInline]
admin.site.register(Payment)
