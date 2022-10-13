# Generated by Django 4.1 on 2022-08-17 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(db_index=True, max_length=20, verbose_name='Имя пользователя')),
                ('password', models.TextField(blank=True, verbose_name='Пользовательский пароль')),
            ],
        ),
    ]
