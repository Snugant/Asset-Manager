# Generated by Django 5.0.3 on 2024-05-29 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AssetManagerApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='space',
            name='pinned',
            field=models.BooleanField(blank=True),
        ),
    ]