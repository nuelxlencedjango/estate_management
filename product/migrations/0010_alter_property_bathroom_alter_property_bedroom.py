# Generated by Django 4.0.2 on 2022-07-20 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0009_contactimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='bathroom',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='bedroom',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
