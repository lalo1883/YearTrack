# Generated by Django 3.2.8 on 2023-12-18 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reading', '0002_books_pages'),
    ]

    operations = [
        migrations.CreateModel(
            name='weekly_track',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hours_read', models.FloatField()),
                ('pages_read', models.IntegerField()),
                ('reflexions', models.TextField()),
            ],
        ),
    ]
