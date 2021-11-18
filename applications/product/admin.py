from django.contrib import admin

from applications.product.models import Product

from applications.product.models import ProductImage


class InlineProductImage(admin.TabularInline):
    model = ProductImage
    extra = 1
    fields = ['image', ]


class ProductAdminDisplay(admin.ModelAdmin):
    inlines = [InlineProductImage, ]


admin.site.register(Product, ProductAdminDisplay)

