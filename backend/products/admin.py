from django.contrib import admin

from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content', 'price', 'public', 'user']
    list_display_links = ['title']
    search_fields = 'id', 'title', 'user',
    list_filter = 'title', 'user', 'public',
    list_per_page = 10
    ordering = '-id',
