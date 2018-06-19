from django.contrib import admin
from .models import TypeInfo, GoodsInfo,Banner

# Register your models here.

admin.site.register(Banner)
admin.site.register(TypeInfo)
admin.site.register(GoodsInfo)
