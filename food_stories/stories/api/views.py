from django.http import JsonResponse, Http404
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from stories.api.serializers import StorySerializer, StoryListSerializer, SubscriberSerializer
from stories.models import Story, Subscriber
from rest_framework.generics import ListCreateAPIView, CreateAPIView


# class StoriesAPIView(APIView):
#     permission_classes = (IsAuthenticatedOrReadOnly,)
#
#     def get(self, *args, **kwargs):
#         stories = Story.objects.all()
#         serializer = StoryListSerializer(stories, many=True, context={'request': self.request})
#         return JsonResponse(data=serializer.data, safe=False)
#
#     def post(self, *args, **kwargs):
#         story_data = self.request.data
#         serializer = StorySerializer(data=story_data, context={'request': self.request})
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return JsonResponse(data=serializer.data, safe=False, status=201)


class StoriesAPIView(ListCreateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Story.objects.filter(is_published=True)
    serializer_class = StoryListSerializer
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return StorySerializer
        return super(StoriesAPIView, self).get_serializer_class()

from rest_framework.parsers import FormParser

class StoryAPIView(GenericAPIView):
    serializer_class = StorySerializer
    parser_classes = (FormParser,)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return StoryListSerializer
        return super().get_serializer_class()


    def get(self, *args, **kwargs):
        story = Story.objects.filter(slug=kwargs.get('slug')).first()
        if not story:
            raise Http404
        serializer = StoryListSerializer(story, context={'request': self.request})
        return JsonResponse(data=serializer.data, safe=False)


    def put(self, *args, **kwargs):
        story = Story.objects.filter(slug=kwargs.get('slug')).first()
        if not story:
            raise Http404
        serializer = StorySerializer(data=self.request.data,
                                     instance=story, context={'request': self.request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return JsonResponse(data=serializer.data, safe=False, status=201)


class SubscribeAPIView(CreateAPIView):
    serializer_class = SubscriberSerializer
    model = Subscriber
