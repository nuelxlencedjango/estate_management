# Generated by Django 4.0.2 on 2022-08-28 09:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0018_rename_user_user_visitors'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='visitors',
            new_name='user',
        ),
    ]
