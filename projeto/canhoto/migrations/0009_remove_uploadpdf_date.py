# Generated by Django 4.1.7 on 2023-04-08 01:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('canhoto', '0008_uploadpdf'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uploadpdf',
            name='date',
        ),
    ]