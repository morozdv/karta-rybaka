# Generated by Django 4.1 on 2022-08-17 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_mapentity_publication_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='path',
            field=models.ImageField(blank=True, upload_to='', verbose_name='Фото'),
        ),
    ]
