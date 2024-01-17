from django.contrib import admin
from .models.products import Product
from .models.category import Category
from .models.customer import Customer
from .models.order import Order
from .models.front import Front

class AdminProduct(admin.ModelAdmin):
    list_display=['name','price','category','description']

class AdminCategory(admin.ModelAdmin):
    list_display=['name']
# Register your models here.
admin.site.register(Product,AdminProduct)
admin.site.register(Category,AdminCategory)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Front)