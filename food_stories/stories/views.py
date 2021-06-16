import math
from datetime import datetime

from django.shortcuts import render
from django.db.models import Q
from stories.models import Book


# http://localhost:8000/books/?p=2
def book_list(request):
    search = request.GET.get('search', '')
    page = int(request.GET.get('p', 1))
    print('searched value', search)
    books = Book.objects.all().order_by('-price')

    # a = [1, 2, 3, 4, 5, 6, 7, 8] [3:6]
    # i = [0, 1, 2, 3, 4, 5, 6, 7]
    # current_page, per_page = 3
    # 1 [0, 3) per_page*(page-1), page*per_page
    # 2 [3, 6)
    # 3 [6, 9)
    if search:
        books = books.filter(Q(title__icontains=search) | Q(author__full_name__icontains=search))
    per_page = 3
    book_count = books.count()
    page_count = math.ceil(book_count / per_page)
    books = books[per_page * (page - 1): page * per_page]  # [0,3]
    previous_page = page - 1 if page > 1 else None
    next_page = page + 1 if page < page_count else None
    book_created_date = datetime(2021, 10, 12, 12, 00, 00)
    html = '<h1>Hello World</h1>'
    context = {
        'book_list': books,
        'html': html,
        'book_created_date': book_created_date,
        'page_count': page_count,
        'page_range': range(1, page_count + 1),
        'current_page': page,
        'previous_page': previous_page,
        'next_page': next_page
    }
    return render(request, 'books.html', context)
