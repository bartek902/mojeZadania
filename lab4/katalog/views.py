from django.shortcuts import render
from django.http import JsonResponse
from .models import Book

# Widok strony HTML
def index(request):
    return render(request, 'katalog/index.html')

# Endpoint API z filtrowaniem ORM
def api_books(request):
    books = Book.objects.all()
    
    # Obsługa filtra po parametrze w URL (?available=true)
    available_filter = request.GET.get('available')
    if available_filter == 'true':
        books = books.filter(is_available=True)
    elif available_filter == 'false':
        books = books.filter(is_available=False)

    # Budowanie struktury JSON
    data = {
        "items": [
            {
                "id": book.id,
                "title": book.title,
                "author": book.author,
                "published_year": book.published_year,
                "is_available": book.is_available
            } for book in books
        ]
    }
    return JsonResponse(data)