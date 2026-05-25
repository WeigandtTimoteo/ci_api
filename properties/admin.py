from django.contrib import admin
from .models import Property, PropertyImage

class PropertyImageInline(admin.TabularInline):
    model = PropertyImage
    extra = 1

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('location', 'price', 'currency', 'age_status', 'is_active', 'created_at')
    list_filter = ('is_active', 'age_status', 'currency')
    search_fields = ('location', 'description')
    inlines = [PropertyImageInline]