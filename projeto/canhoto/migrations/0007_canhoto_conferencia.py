# Generated by Django 4.1.7 on 2023-03-16 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('canhoto', '0006_alter_canhoto_codigo'),
    ]

    operations = [
        migrations.AddField(
            model_name='canhoto',
            name='conferencia',
            field=models.BooleanField(default=False, verbose_name='conferência'),
        ),
    ]
