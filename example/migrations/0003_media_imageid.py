# Generated by Django 4.1.3 on 2024-03-29 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('example', '0002_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='media',
            name='imageId',
            field=models.UUIDField(null=True),
        ),
    ]
