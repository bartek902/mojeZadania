from django.shortcuts import render
from django.http import JsonResponse
from .models import Book

def index(request):
    return render(request, 'katalog/index.html')

def api_books(request):
    
    books = Book.objects.filter(pages__gte=0) 
    
    available_filter = request.GET.get('available')
    if available_filter == 'true':
        books = books.filter(is_available=True)
    elif available_filter == 'false':
        books = books.filter(is_available=False)

    books = books.order_by('title')

    books = books[:5]

    data = {
        "items": [
            {
                "id": book.id,
                "title": book.title,
                "author": book.author,
                "category": book.category,      
                "pages": book.pages,          
                "published_year": book.published_year,
                "is_available": book.is_available
            } for book in books
        ]
    }
    return JsonResponse(data)       