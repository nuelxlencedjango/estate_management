# Generated by Django 4.0.2 on 2022-07-20 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0013_featuredimages'),
    ]

    operations = [
        migrations.AddField(
            model_name='featuredlisting',
            name='description',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
    ]
