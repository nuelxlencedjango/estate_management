# Generated by Django 4.0.2 on 2022-07-20 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0010_alter_property_bathroom_alter_property_bedroom'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='describe',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
    ]
