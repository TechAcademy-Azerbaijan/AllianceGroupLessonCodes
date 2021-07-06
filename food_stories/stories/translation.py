from modeltranslation.translator import translator, TranslationOptions
from .models import Story, Category


class StoryTranslationOptions(TranslationOptions):
    fields = ('title', 'slug', 'description')
    required_languages = ('en', 'az', 'ru')


class CategoryTranslationOptions(TranslationOptions):
    fields = ('title',)


translator.register(Story, StoryTranslationOptions)
translator.register(Category, CategoryTranslationOptions)
