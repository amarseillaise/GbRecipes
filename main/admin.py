from django.contrib import admin
from .models import Recipe, Category

# Register your models here.


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    all_fields = ('id', 'name', 'description', 'cooking_time', 'cooking_descr', 'origin_country', 'image')
    list_display = all_fields
    ordering = all_fields
    list_filter = ('cooking_time',)
    list_display_links = ('name',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    all_fields = ('id', 'name')
    list_display = all_fields
    ordering = all_fields
