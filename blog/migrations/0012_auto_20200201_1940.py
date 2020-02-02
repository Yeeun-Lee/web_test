# Generated by Django 3.0.2 on 2020-02-01 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20200201_1924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='slug',
            field=models.SlugField(default='FHSDLl', max_length=6, unique=True, verbose_name='slug'),
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(default='cjSHMu', max_length=6, unique=True, verbose_name='slug'),
        ),
    ]