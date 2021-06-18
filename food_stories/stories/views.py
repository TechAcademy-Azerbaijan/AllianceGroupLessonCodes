import math
from datetime import datetime

from django.contrib import messages
from django.shortcuts import render, redirect
from django.db.models import Q

from stories.forms import ContactForm
from stories.models import Book, Category


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
    html = """
    Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
    """
    a = 4
    context = {
        'book_list': books,
        'html': html,
        'book_created_date': book_created_date,
        'page_count': page_count,
        'page_range': range(1, page_count + 1),
        'current_page': page,
        'previous_page': previous_page,
        'next_page': next_page,
        'a': a,
    }
    return render(request, 'books.html', context)


def index(request):
    return render(request, 'index.html')


def contact(request):
    form = ContactForm()

    if request.method == 'POST':
        contact_data = request.POST
        form = ContactForm(data=contact_data)
        if form.is_valid():
            print('data saved')
            form.save()
            messages.success(request, 'Muracietiniz qebul olundu')
            return redirect('/')
    context = {
        'form': form
    }
    return render(request, 'contact.html', context)
