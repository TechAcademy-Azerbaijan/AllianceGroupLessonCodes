from django.test import TestCase
from stories.forms import ContactForm

class ContactFormTest(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.valid_data = {
            'name': 'Idris Shabanli',
            'email': 'idris@gmail.com',
            'subject': 'Sayt islemir',
            'message': 'Ana sehifeden login sehifesine daxil ola bilmirem'
        }

        cls.invalid_data = {
            'email': 'idrissjlknfsldknfsfnndslkfnsdfjksdfjsbdfjsbdfjksbdfjkbdfbjkdbfjdbjfbkdbjfbdjk@gmail.com',
            'subject': 'Sayt islemir',
            'message': 'Ana sehifeden login sehifesine daxil ola bilmirem'
        }

    def test_form_with_valid_data(self):
        form = ContactForm(data=self.valid_data)
        self.assertTrue(form.is_valid())

    def test_form_with_invalid_data(self):
        form = ContactForm(data=self.invalid_data)
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors)
        self.assertIn('email', form.errors)
        self.assertIn('Bu sahə tələb edilir.', form.errors['name'])
        self.assertIn('Bu dəyərin ən çox 40 simvol olduğuna əmin olun (87 var)', form.errors['email'])



    @classmethod
    def tearDownClass(cls):
        pass


