from django.db import models
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(_('email address'), unique=True,)
    GENDER_CHOICES = (
        (True, 'Men'),
        (False, 'Woman'),
    )
    image = models.ImageField('Image', upload_to='profile_pictures', max_length=500, null=True, blank=True)
    bio = models.TextField('Bio', null=True, blank=True)
    gender = models.BooleanField('Gender', choices=GENDER_CHOICES, default=False)
