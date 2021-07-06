from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.defaultfilters import slugify
from stories.models import Story, Recipe
from django.utils import timezone


@receiver(post_save, sender=Story)
def story_set_slug(sender, instance, created, *args, **kwargs):
    if created:
        instance.slug_az = f"{slugify(instance.title_az)}-{instance.id}"
        instance.slug_en = f"{slugify(instance.title_en)}-{instance.id}"
        instance.slug_ru = f"{slugify(instance.title_ru)}-{instance.id}"
        instance.save()

