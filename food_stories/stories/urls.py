from django.urls import path
from stories.views import (
    book_list,
    index,
    contact
)

app_name = 'stories'

urlpatterns = [
    path('books/', book_list, name='book_list'),
    path('', index, name='index'),
    path('contact/', contact, name='contact'),
]