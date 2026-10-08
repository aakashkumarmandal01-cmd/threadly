from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Category(models.Model):
    name=models.CharField(max_length=120); slug=models.SlugField(unique=True); parent=models.ForeignKey('self',null=True,blank=True,on_delete=models.CASCADE,related_name='children'); is_active=models.BooleanField(default=True); sort_order=models.PositiveIntegerField(default=0)
    class Meta: ordering=['sort_order','name']
    def __str__(self): return self.name
class Brand(models.Model): name=models.CharField(max_length=100,unique=True); is_active=models.BooleanField(default=True)
class Size(models.Model): name=models.CharField(max_length=30,unique=True)
class Color(models.Model): name=models.CharField(max_length=50); hex_code=models.CharField(max_length=7,default='#000000')
class Product(models.Model):
    name=models.CharField(max_length=220); sku=models.CharField(max_length=80,unique=True); brand=models.ForeignKey(Brand,null=True,blank=True,on_delete=models.SET_NULL)
    category=models.ForeignKey(Category,on_delete=models.PROTECT,related_name='products'); short_description=models.CharField(max_length=500,blank=True); description=models.TextField(blank=True)
    material=models.CharField(max_length=120,blank=True); gender=models.CharField(max_length=30,blank=True); age_group=models.CharField(max_length=30,blank=True); tags=models.CharField(max_length=500,blank=True)
    original_price=models.DecimalField(max_digits=12,decimal_places=2); selling_price=models.DecimalField(max_digits=12,decimal_places=2)
    return_eligible=models.BooleanField(default=True); return_days=models.PositiveIntegerField(default=7); is_published=models.BooleanField(default=True); created_at=models.DateTimeField(auto_now_add=True); updated_at=models.DateTimeField(auto_now=True)
    def __str__(self): return self.name
    @property
    def discount_percent(self): return round((1-self.selling_price/self.original_price)*100,2) if self.original_price else 0
    @property
    def average_rating(self):
        x=self.reviews.filter(is_approved=True).aggregate(v=models.Avg('rating'))['v']; return round(x or 0,1)
class ProductImage(models.Model): product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name='images'); image=models.ImageField(upload_to='products/%Y/%m/'); alt_text=models.CharField(max_length=200,blank=True); sort_order=models.PositiveIntegerField(default=0)
class ProductVariant(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name='variants'); size=models.ForeignKey(Size,null=True,blank=True,on_delete=models.PROTECT); color=models.ForeignKey(Color,null=True,blank=True,on_delete=models.PROTECT); sku=models.CharField(max_length=100,unique=True); stock=models.PositiveIntegerField(default=0); reserved=models.PositiveIntegerField(default=0); low_stock_threshold=models.PositiveIntegerField(default=5)
    class Meta: constraints=[models.UniqueConstraint(fields=['product','size','color'],name='unique_product_variant')]
    @property
    def available_stock(self): return max(0,self.stock-self.reserved)
