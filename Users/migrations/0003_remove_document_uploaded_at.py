# Generated by Django 3.1 on 2020-10-25 13:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0002_document'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='uploaded_at',
        ),
    ]
