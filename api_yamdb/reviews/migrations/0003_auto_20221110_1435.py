# Generated by Django 2.2.16 on 2022-11-10 11:35

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_auto_20221109_2257'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='title',
            name='rating',
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(unique=True, validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z]*$', 'Допустимы только буквы или цифры.')]),
        ),
        migrations.AlterField(
            model_name='genre',
            name='slug',
            field=models.SlugField(unique=True, validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z]*$', 'Допустимы только буквы или цифры.')]),
        ),
    ]
