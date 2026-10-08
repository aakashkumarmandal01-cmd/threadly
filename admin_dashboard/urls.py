from django.urls import path
from .views import dashboard, products
urlpatterns=[path('dashboard/',dashboard,name='admin_dashboard'),path('products/',products,name='admin_products')]
