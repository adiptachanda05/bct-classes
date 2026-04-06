from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'status', 'created_at')
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'price', 'image', 'description', 'status')
        }),
        ('Specifications', {
            'fields': ('specifications',),
            'description': 'Enter specifications as JSON. Example: [{"icon": "💻", "label": "Processor", "value": "Intel i7"}, {"icon": "⚡", "label": "RAM", "value": "16GB"}]'
        }),
        ('Metadata', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )
    readonly_fields = ('created_at',)

admin.site.register(Product, ProductAdmin)


