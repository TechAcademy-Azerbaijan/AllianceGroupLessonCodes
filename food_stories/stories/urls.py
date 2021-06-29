from django.urls import path
from stories.views import (
    book_list,
    index,
    ContactView,
    StoriesView,
    StoryDetailView
)

app_name = 'stories'

urlpatterns = [
    path('books/', book_list, name='book_list'),
    path('', index, name='index'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('stories/', StoriesView.as_view(), name='stories'),
    path('stories/<int:pk>/', StoryDetailView.as_view(), name='story_detail'),
]