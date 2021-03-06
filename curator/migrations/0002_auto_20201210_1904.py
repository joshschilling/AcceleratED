# Generated by Django 3.1.4 on 2020-12-10 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curator', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='date_added',
        ),
        migrations.RemoveField(
            model_name='book',
            name='year',
        ),

        migrations.AddField(
            model_name='book',
            name='owner',
            field=models.CharField(blank=True, max_length=150),
        ),

        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.CharField(blank=True, max_length=60),
        ),
        migrations.AlterField(
            model_name='book',
            name='comment',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=models.CharField(blank=True, max_length=60),
        ),
        migrations.AlterField(
            model_name='book',
            name='publisher',
            field=models.CharField(blank=True, max_length=60),
        ),

    ]
