from django.contrib import admin
from stories.models import (
    Category,
    Story,
    Tag,
    Recipe,
    RecipeComment,
    StoryComment,
    Book,
    Author
)


class RecipeCommentInlineAdmin(admin.TabularInline):
    model = RecipeComment
    extra = 10


class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'author', 'get_category_image', 'is_published', 'created_at')
    list_filter = ('category__title', 'is_published',)
    search_fields = ('title', 'author__username')
    ordering = ('-title',)
    inlines = (RecipeCommentInlineAdmin, )

    # def get_queryset(self, request):
    #     if request.user.username == 'kamal':
    #         return super().get_queryset(request).filter(is_published=True)
    #     return super().get_queryset(request)
    # fieldsets = (
    #     ('Relations', {
    #         'fields': ('tags', 'author', 'category')
    #     }),
    #     ('Information', {
    #         'classes': ('collapse', 'open'),
    #         'fields': ('title', 'short_description', 'description', 'image',)
    #     }),
    # )
    # fields = (
    #     'title',
    #     ('category', 'author'),
    #     'tags',
    # )

    def get_category_image(self, obj):
        return obj.category.image

    get_category_image.short_description = 'Category Image'


@admin.register(RecipeComment)
class RecipeCommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'content', 'recipe', 'parent_comment', 'created_at', 'is_published')


from django.utils.html import format_html

logo_url= "https://static.wixstatic.com/media/50b774_7148e9bb84e04e4fb77a11ca94709cac~mv2.jpg/v1/fit/w_2500,h_1330,al_c/50b774_7148e9bb84e04e4fb77a11ca94709cac~mv2.jpg"
admin.site.site_header = format_html("`<img src={url} height=100 width=100`>", url=logo_url)

admin.site.register(Recipe, RecipeAdmin)
admin.site.register([Category, Story, Tag,
                     StoryComment,
                     Book,
                     Author
                     ])
