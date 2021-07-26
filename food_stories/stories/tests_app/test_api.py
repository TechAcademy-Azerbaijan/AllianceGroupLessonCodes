from django.conf import settings
from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
# from django.
from stories.api.serializers import StoryListSerializer
from stories.models import Category, Story


User = get_user_model()

class StoryDetailTest(TestCase):

    @classmethod
    def setUpClass(cls):
        cat1 = Category.objects.create(title='Cat 1', image='cat1.png')
        user = User.objects.create_user(username='afklndsklfn',
                                        first_name='sdlknf', last_name='sndfsdfk',
                                        email='email@gmail.com',
                                        password='qwsxcdqdxcws1S'
                                        )
        cls.story = Story.objects.create(title='Story 1',
                                         description='description',
                                         category=cat1,
                                         author=user,
                                         image='story.png',
                                         )
        cls.url = reverse_lazy('stories_api:story_detail', kwargs={'slug': cls.story.slug})
        cls.expected_url = f"/api/stories/{cls.story.slug}/"

    def test_url(self):
        self.assertEqual(self.url, self.expected_url)

    def test_response_status_code(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_response_body(self):
        response = self.client.get(self.url)
        # print(response.headers)
        self.assertEqual(response['Content-Type'], 'application/json')
        serializer = StoryListSerializer(self.story)
        data = dict(serializer.data)
        self.assertEqual(data.keys(), response.json().keys())

    @classmethod
    def tearDownClass(cls):
        pass
