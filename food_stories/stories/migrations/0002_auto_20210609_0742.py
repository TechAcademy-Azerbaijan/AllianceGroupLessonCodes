# Generated by Django 2.2.8 on 2021-06-09 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='story',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Mezmun'),
        ),
        migrations.AlterField(
            model_name='story',
            name='image',
            field=models.ImageField(upload_to='media/story_images/', verbose_name='Sekil'),
        ),
        migrations.AlterField(
            model_name='story',
            name='is_published',
            field=models.BooleanField(default=False, verbose_name='Ders olunsun?'),
        ),
        migrations.AlterField(
            model_name='story',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
