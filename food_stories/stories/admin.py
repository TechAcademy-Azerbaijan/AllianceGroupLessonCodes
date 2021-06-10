from django.contrib import admin
from stories.models import (
    Category,
    Story,
    Tag,
    Recipe,
    RecipeComment,
    StoryComment
)


@admin.register(RecipeComment)
class RecipeCommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'content', 'recipe', 'parent_comment', 'created_at', 'is_published')


admin.site.register([Category, Story, Tag, Recipe,
                     StoryComment])
