from django.urls import path

from stories.api.views import StoriesAPIView, StoryAPIView

app_name = 'stories_api'

urlpatterns = [
    path('stories/', StoriesAPIView.as_view(), name='stories'),
    path('stories/<slug:slug>/', StoryAPIView.as_view(), name='story_detail'),
]
