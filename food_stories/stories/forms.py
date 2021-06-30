from django import forms

from stories.models import Contact, Story


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = (
            'name',
            'email',
            'subject',
            'message'
        )

        widgets = {
            'name': forms.TextInput(attrs={
                               'class': 'form-control',
                               'placeholder': 'Your name'
                           }),
            'email': forms.EmailInput(attrs={
                                 'class': 'form-control',
                                 'placeholder': 'Your email'
                             }),
            'subject': forms.TextInput(attrs={
                                  'class': 'form-control',
                                  'placeholder': 'Write subject'
                              }),
            'message': forms.Textarea(attrs={
                                  'class': 'form-control',
                                  'placeholder': 'Your message'
                              })
        }

    # def clean_email(self):

    def clean(self):
        email = self.cleaned_data['email']
        if not email.endswith('gmail.com'):
            raise forms.ValidationError('Yalniz gmail.com saytindan olan emailler qebul edilir')
        return super().clean()


class StoryForm(forms.ModelForm):
    class Meta:
        model = Story
        fields = (
            'title',
            'description',
            'category',
            'tags',
            'image'
        )

        widgets = {
            'title': forms.TextInput(attrs={
                               'class': 'form-control',
                               'placeholder': 'Title'
                           }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Description'
            }),
            'category': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Category'
            }),
            'tags': forms.SelectMultiple(attrs={
                'class': 'form-control',
                'placeholder': 'Tags'
            }),
        }


    # name = forms.CharField(max_length=40, required=True, label='Name',
    #                        widget=forms.TextInput(attrs={
    #                            'class': 'form-control',
    #                            'placeholder': 'Your name'
    #                        }))
    # email = forms.EmailField(max_length=40, required=True, label='Email',
    #                          widget=forms.EmailInput(attrs={
    #                              'class': 'form-control',
    #                              'placeholder': 'Your email'
    #                          }))
    # subject = forms.CharField(max_length=255, required=True, label='Subject',
    #                           widget=forms.TextInput(attrs={
    #                               'class': 'form-control',
    #                               'placeholder': 'Write subject'
    #                           }))
    # message = forms.CharField(required=True, label='Message',
    #                           widget=forms.Textarea(attrs={
    #                               'class': 'form-control',
    #                               # 'rows': 100,
    #                               'placeholder': 'Your message'
    #                           }))

