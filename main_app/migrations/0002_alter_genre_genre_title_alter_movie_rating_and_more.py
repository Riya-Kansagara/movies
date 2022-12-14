# Generated by Django 4.1.2 on 2022-10-08 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genre',
            name='genre_title',
            field=models.CharField(max_length=40, unique=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='rating',
            field=models.IntegerField(default=0, verbose_name='rating'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='title',
            field=models.CharField(max_length=250, unique=True, verbose_name='movie title'),
        ),
    ]
