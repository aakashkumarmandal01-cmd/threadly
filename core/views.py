from django.db.models import Q
from django.shortcuts import get_object_or_404, render
from products.models import Product, Category

def home(request):
    products=Product.objects.filter(is_published=True).select_related('brand','category').prefetch_related('images','variants')
    return render(request,'home.html',{'featured':products.order_by('-created_at')[:8],'best_sellers':products[:8],'categories':Category.objects.filter(is_active=True,parent__isnull=True)})
def product_list(request):
    qs=Product.objects.filter(is_published=True).select_related('brand','category')
    q=request.GET.get('q','').strip(); category=request.GET.get('category',''); sort=request.GET.get('sort','newest')
    if q: qs=qs.filter(Q(name__icontains=q)|Q(sku__icontains=q)|Q(tags__icontains=q)|Q(description__icontains=q)|Q(brand__name__icontains=q))
    if category: qs=qs.filter(category__slug=category)
    if sort=='price_low': qs=qs.order_by('selling_price')
    elif sort=='price_high': qs=qs.order_by('-selling_price')
    elif sort=='rating': qs=qs.order_by('-reviews__rating')
    else: qs=qs.order_by('-created_at')
    return render(request,'products/list.html',{'products':qs.distinct(),'categories':Category.objects.filter(is_active=True),'q':q})
def search(request): return product_list(request)
def product_detail(request,pk): return render(request,'products/detail.html',{'product':get_object_or_404(Product,pk=pk,is_published=True)})
