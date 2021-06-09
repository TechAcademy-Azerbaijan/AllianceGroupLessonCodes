from django.contrib import admin
from stories.models import (
    Category,
    Story,
    Tag
)

admin.site.register([Category, Story, Tag])
