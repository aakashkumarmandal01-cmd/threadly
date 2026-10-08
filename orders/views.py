from decimal import Decimal
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.shortcuts import get_object_or_404, redirect, render
from .models import Order, OrderItem
from cart.models import Cart
import uuid
@login_required
def checkout(request):
    cart=get_object_or_404(Cart.objects.prefetch_related('items__variant__product'),user=request.user); items=list(cart.items.all())
    if not items: return redirect('cart')
    if request.method=='POST':
        required=['shipping_name','shipping_phone','shipping_line1','shipping_city','shipping_state','shipping_pincode']; data={k:request.POST.get(k,'').strip() for k in required}
        if not all(data.values()): return render(request,'orders/checkout.html',{'cart':cart,'error':'Please complete the shipping address.'})
        with transaction.atomic():
            for i in items:
                i.variant.refresh_from_db()
                if i.quantity>i.variant.available_stock: return render(request,'orders/checkout.html',{'cart':cart,'error':f'Insufficient stock for {i.variant.product.name}.'})
            subtotal=sum(i.variant.product.selling_price*i.quantity for i in items); shipping=Decimal('0') if subtotal>=999 else Decimal('79'); tax=(subtotal*Decimal('.05')).quantize(Decimal('.01')); total=subtotal+shipping+tax
            o=Order.objects.create(user=request.user,order_id='ORD-'+uuid.uuid4().hex[:10].upper(),shipping_name=data['shipping_name'],shipping_phone=data['shipping_phone'],shipping_line1=data['shipping_line1'],shipping_city=data['shipping_city'],shipping_state=data['shipping_state'],shipping_pincode=data['shipping_pincode'],subtotal=subtotal,shipping_fee=shipping,tax=tax,total=total,payment_method=request.POST.get('payment_method','cod'))
            for i in items:
                i.variant.stock-=i.quantity; i.variant.save(update_fields=['stock']); OrderItem.objects.create(order=o,variant=i.variant,product_name=i.variant.product.name,size=i.variant.size.name if i.variant.size else '',color=i.variant.color.name if i.variant.color else '',quantity=i.quantity,unit_price=i.variant.product.selling_price)
            cart.items.all().delete()
        return redirect('order_detail',pk=o.pk)
    return render(request,'orders/checkout.html',{'cart':cart})
@login_required
def my_orders(request): return render(request,'orders/orders.html',{'orders':request.user.orders.all()})
@login_required
def order_detail(request,pk): return render(request,'orders/detail.html',{'order':get_object_or_404(Order,pk=pk,user=request.user)})
