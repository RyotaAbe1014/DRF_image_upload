# Generated by Django 3.2 on 2022-06-30 12:25

import api.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('top_image', models.ImageField(blank=True, null=True, upload_to=api.models.top_image_upload_path, verbose_name='トップ画像')),
            ],
        ),
    ]
