# Generated by Django 4.0.2 on 2022-06-23 21:12

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_rename_position_ourteam_positions'),
    ]

    operations = [
        migrations.CreateModel(
            name='contactImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]
