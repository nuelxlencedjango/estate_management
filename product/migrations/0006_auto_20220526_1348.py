# Generated by Django 3.2 on 2022-05-26 13:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_auto_20220416_2033'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Banner',
        ),
        migrations.DeleteModel(
            name='Brand',
        ),
        migrations.DeleteModel(
            name='Color',
        ),
        migrations.DeleteModel(
            name='EmpModel',
        ),
        migrations.RemoveField(
            model_name='studentinfo',
            name='department',
        ),
        migrations.DeleteModel(
            name='Department',
        ),
        migrations.DeleteModel(
            name='StudentInfo',
        ),
    ]