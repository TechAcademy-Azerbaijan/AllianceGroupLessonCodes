# Generated by Django 2.2.8 on 2021-07-02 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(blank=True, max_length=500, null=True, upload_to='profile_pictures', verbose_name='Image'),
        ),
    ]
