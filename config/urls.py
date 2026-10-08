from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from core.views import home, product_list, product_detail, search
from accounts.views import register, profile
from cart.views import cart_detail, add_to_cart, remove_from_cart, update_cart
from orders.views import checkout, order_detail, my_orders

urlpatterns = [
    path('django-admin/', admin.site.urls),
    path('', home, name='home'),
    path('products/', product_list, name='product_list'),
    path('product/<int:pk>/', product_detail, name='product_detail'),
    path('search/', search, name='search'),
    path('', include('django.contrib.auth.urls')),
    path('register/', register, name='register'), path('profile/', profile, name='profile'),
    path('cart/', cart_detail, name='cart'), path('cart/add/<int:variant_id>/', add_to_cart, name='cart_add'),
    path('cart/remove/<int:item_id>/', remove_from_cart, name='cart_remove'), path('cart/update/<int:item_id>/', update_cart, name='cart_update'),
    path('checkout/', checkout, name='checkout'), path('orders/', my_orders, name='orders'), path('order/<int:pk>/', order_detail, name='order_detail'),
    path('api/', include('products.api_urls')),
    path('admin-panel/', include('admin_dashboard.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
