from django.urls import path

from stories.api.views import StoriesAPIView, StoryAPIView, SubscribeAPIView

app_name = 'stories_api'

urlpatterns = [
    path('stories/', StoriesAPIView.as_view(), name='stories'),
    path('subscribe/', SubscribeAPIView.as_view(), name='subscribe'),
    path('stories/<slug:slug>/', StoryAPIView.as_view(), name='story_detail'),
]
