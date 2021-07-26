from django.conf import settings
from django.test import TestCase
from django.urls import reverse_lazy

from stories.models import Contact


class ContactViewTest(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.url = reverse_lazy('stories:contact')
        cls.valid_data = {
            'name': 'Idris Shabanli',
            'email': 'idris@gmail.com',
            'subject': 'Sayt islemir',
            'message': 'Ana sehifeden login sehifesine daxil ola bilmirem'
        }

        cls.invalid_data = {
            'name': 'Idris Shabanli',
            'email': 'idris',
            'subject': 'Sayt islemir',
            'message': 'Ana sehifeden login sehifesine daxil ola bilmirem'
        }
        cls.contact_url = f'/{settings.LANGUAGE_CODE}/contact/'

    def test_url(self):

        self.assertEqual(self.url, self.contact_url)

    def test_get_request(self):
        response = self.client.get(self.contact_url)
        self.assertEqual(response.status_code, 200)
        self.assertIn('form', response.context)
        self.assertTemplateUsed(response, 'contact.html')

    def test_post_request(self):
        response = self.client.post(self.url, self.valid_data)
        self.assertEqual(response.status_code, 302)
        contact_data = Contact.objects.last()
        self.assertEqual(self.valid_data['name'], contact_data.name)
        self.assertEqual(self.valid_data['email'], contact_data.email)
        self.assertEqual(self.valid_data['message'], contact_data.message)
        self.assertRedirects(response, f'/{settings.LANGUAGE_CODE}/')

    def test_post_invalid_request(self):
        response = self.client.post(self.url, self.invalid_data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Keçərli e-poçt ünvanı daxil edin.", html=True)

    @classmethod
    def tearDownClass(cls):
        pass
