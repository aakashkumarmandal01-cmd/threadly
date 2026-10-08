from django.contrib.admin.views.decorators import staff_member_required
from django.db.models import Sum,Count
from django.shortcuts import render
from orders.models import Order
from products.models import Product,ProductVariant
@staff_member_required
def dashboard(request):
    orders=Order.objects.all(); revenue=orders.filter(status='delivered').aggregate(v=Sum('total'))['v'] or 0
    return render(request,'admin_dashboard/dashboard.html',{'revenue':revenue,'orders':orders.count(),'customers':__import__('accounts.models',fromlist=['User']).User.objects.filter(is_customer=True).count(),'products':Product.objects.count(),'low_stock':ProductVariant.objects.filter(stock__lte=5,stock__gt=0).count(),'recent':orders.order_by('-created_at')[:10]})
@staff_member_required
def products(request): return render(request,'admin_dashboard/products.html',{'products':Product.objects.select_related('category','brand').order_by('-created_at')})
