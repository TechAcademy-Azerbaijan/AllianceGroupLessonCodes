from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.defaultfilters import slugify
from stories.models import Story, Recipe
from django.utils import timezone


@receiver(post_save, sender=Story)
def story_set_slug(sender, instance, created, *args, **kwargs):
    if created:
        instance.slug = f"{slugify(instance.title)}-{instance.id}"
        instance.save()

