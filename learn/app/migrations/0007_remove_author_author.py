# Generated by Django 5.1.4 on 2025-01-14 07:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_book_publication_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='author',
        ),
    ]
