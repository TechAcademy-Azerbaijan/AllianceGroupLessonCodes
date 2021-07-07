# Generated by Django 2.2.8 on 2021-07-06 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0002_auto_20210705_0633'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='title_az',
            field=models.CharField(max_length=40, null=True, verbose_name='Basliq'),
        ),
        migrations.AddField(
            model_name='category',
            name='title_en',
            field=models.CharField(max_length=40, null=True, verbose_name='Basliq'),
        ),
        migrations.AddField(
            model_name='category',
            name='title_ru',
            field=models.CharField(max_length=40, null=True, verbose_name='Basliq'),
        ),
        migrations.AddField(
            model_name='story',
            name='description_az',
            field=models.TextField(blank=True, null=True, verbose_name='Mezmun'),
        ),
        migrations.AddField(
            model_name='story',
            name='description_en',
            field=models.TextField(blank=True, null=True, verbose_name='Mezmun'),
        ),
        migrations.AddField(
            model_name='story',
            name='description_ru',
            field=models.TextField(blank=True, null=True, verbose_name='Mezmun'),
        ),
        migrations.AddField(
            model_name='story',
            name='title_az',
            field=models.CharField(max_length=120, null=True, verbose_name='Title'),
        ),
        migrations.AddField(
            model_name='story',
            name='title_en',
            field=models.CharField(max_length=120, null=True, verbose_name='Title'),
        ),
        migrations.AddField(
            model_name='story',
            name='title_ru',
            field=models.CharField(max_length=120, null=True, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='story',
            name='title',
            field=models.CharField(max_length=120, verbose_name='Title'),
        ),
    ]