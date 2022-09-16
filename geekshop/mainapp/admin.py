from django.contrib import admin
from mainapp.models import ProductCategory, Product

# admin.site.register(Product)
admin.site.register(ProductCategory)

@admin.register(Product)
class Product(admin.ModelAdmin):

    list_display = ('name', 'category', 'quantity', 'price')

    fields = ('name', 'image', 'description', ('price', 'quantity'), 'category')

    readonly_fields = ('description',)

    ordering = ('name', 'category')

    search_fields = ('name',)
