# Generated by Django 3.2 on 2022-02-14 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_alter_studentinfo_cgpa'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmpModel',
            fields=[
                ('empid', models.IntegerField(primary_key=True, serialize=False)),
                ('empname', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('salary', models.IntegerField()),
            ],
            options={
                'db_table': 'employee',
            },
        ),
    ]
