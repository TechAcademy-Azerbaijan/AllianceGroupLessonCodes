from django.core.management.base import BaseCommand
from django.template.defaultfilters import slugify

from stories.models import Story, Recipe


class Command(BaseCommand):
    help = 'This command helps to set recipes and stories slugs'

    def add_arguments(self, parser):
        parser.add_argument('-m', '--model', type=str, help='define you model')  # recipe, story

    def handle(self, *args, **kwargs):
        model = kwargs['model']
        print('here')
        print(model)
        if model.lower() == 'story':
            stories = Story.objects.all()
            for story in stories:
                story.slug = f"{slugify(story.title)}-{story.id}"
                story.save()
        elif model.lower() == 'recipe':
            recipes = Recipe.objects.all()
            for recipe in recipes:
                recipe.slug = f"{slugify(recipe.title)}-{recipe.id}"
                recipe.save()



