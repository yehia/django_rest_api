from django.contrib import admin

from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content', 'price']
    list_display_links = ['title', 'content', 'price']
    search_fields = 'id', 'title',
    list_filter = 'title',
    list_per_page = 10
    ordering = '-id',
