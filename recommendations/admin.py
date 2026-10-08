from django.contrib import admin
from .models import RecentlyViewed,SearchHistory
admin.site.register([RecentlyViewed,SearchHistory])
