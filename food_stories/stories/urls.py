from django.urls import path
from stories.views import (
    book_list,
    index,
    ContactView,
    StoriesView,
    StoryDetailView, CreateStoryView, UpdateStoryView, DeleteStoryView
)

app_name = 'stories'

urlpatterns = [
    path('books/', book_list, name='book_list'),
    path('', index, name='index'),
    # path('dump/', dump_database, ),
    path('contact/', ContactView.as_view(), name='contact'),
    path('stories/', StoriesView.as_view(), name='stories'),
    path('create-story/', CreateStoryView.as_view(), name='create-story'),
    path('update-story/<int:pk>/', UpdateStoryView.as_view(), name='update-story'),
    path('delete-story/<int:pk>/', DeleteStoryView.as_view(), name='delete-story'),
    path('stories/<slug:slug>/', StoryDetailView.as_view(), name='story_detail'),
]