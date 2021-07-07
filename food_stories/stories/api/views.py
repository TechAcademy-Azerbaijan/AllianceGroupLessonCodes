from django.http import JsonResponse, Http404
from rest_framework.views import APIView

from stories.api.serializers import StorySerializer, StoryListSerializer
from stories.models import Story


class StoriesAPIView(APIView):
    def get(self, *args, **kwargs):
        stories = Story.objects.all()
        serializer = StoryListSerializer(stories, many=True, context={'request': self.request})
        return JsonResponse(data=serializer.data, safe=False)

    def post(self, *args, **kwargs):
        story_data = self.request.data
        serializer = StorySerializer(data=story_data, context={'request': self.request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return JsonResponse(data=serializer.data, safe=False, status=201)


class StoryAPIView(APIView):
    def get(self, *args, **kwargs):
        # print(kwargs.get('slug'))
        story = Story.objects.filter(slug=kwargs.get('slug')).first()
        # print(story)
        if not story:
            raise Http404
        serializer = StoryListSerializer(story, context={'request': self.request})
        return JsonResponse(data=serializer.data, safe=False)

