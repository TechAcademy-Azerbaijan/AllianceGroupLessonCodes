from django.shortcuts import render
from django.db.models import Q
from stories.models import Book


def book_list(request):
    search = request.GET.get('search')
    print('searched value', search)
    books = Book.objects.all().order_by('-price')
    if search:
        books = books.filter(Q(title__icontains=search) | Q(author__full_name__icontains=search))

    context = {
        'book_list': books,
    }
    return render(request, 'books.html', context)
