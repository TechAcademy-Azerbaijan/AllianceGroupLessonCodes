from django.test import TestCase
from stories.models import Contact


class ContactModelTest(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.data = {
            'name': 'Idris Shabanli',
            'email': 'idris@gmail.com',
            'subject': 'Sayt islemir',
            'message': 'Ana sehifeden login sehifesine daxil ola bilmirem'
        }
        cls.data2 = {
            'name': 'Yusif Huseynli',
            'email': 'yusif@gmail.com',
            'subject': 'Sayt islemir',
            'message': 'Ana sehifeden login sehifesine daxil ola bilmirem'
        }
        Contact.objects.create(**cls.data)
        Contact.objects.create(**cls.data2)
        cls.contact_info1 = Contact.objects.first()
        cls.contact_info2 = Contact.objects.last()

    def test_created_data(self):
        self.assertEqual(self.contact_info1.name, 'Idris Shabanli')
        self.assertEqual(self.contact_info2.email, self.data2['email'])

    def test_str_method(self):
        self.assertEqual(str(self.contact_info1), self.data['name'])
        self.assertEqual(str(self.contact_info2), self.data2['name'])

    @classmethod
    def tearDownClass(cls):
        print('tearDownClass')
