from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from .models import Cart, CartItem
from products.models import ProductVariant
@login_required
def cart_detail(request):
    cart,_=Cart.objects.get_or_create(user=request.user); total=sum(i.variant.product.selling_price*i.quantity for i in cart.items.select_related('variant__product')); return render(request,'cart/cart.html',{'cart':cart,'total':total})
@login_required
def add_to_cart(request,variant_id):
    v=get_object_or_404(ProductVariant,pk=variant_id); cart,_=Cart.objects.get_or_create(user=request.user); item,_=CartItem.objects.get_or_create(cart=cart,variant=v); item.quantity=min(item.quantity+int(request.POST.get('quantity',1)),v.available_stock); item.save(); return redirect('cart')
@login_required
def remove_from_cart(request,item_id): get_object_or_404(CartItem,pk=item_id,cart__user=request.user).delete(); return redirect('cart')
@login_required
def update_cart(request,item_id):
    item=get_object_or_404(CartItem,pk=item_id,cart__user=request.user); item.quantity=max(1,min(int(request.POST.get('quantity',1)),item.variant.available_stock)); item.save(); return redirect('cart')
