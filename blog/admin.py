from django.contrib import admin
from .models import Category

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category')
    list_display_links = ('id',)
    search_fields = ('id', 'category')
    list_editable = ('category',)


admin.site.register(Category, CategoryAdmin)
