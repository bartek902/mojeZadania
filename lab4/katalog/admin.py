from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    
    list_display = ('title', 'author', 'category', 'pages', 'is_available')
    
    list_filter = ('is_available', 'category')