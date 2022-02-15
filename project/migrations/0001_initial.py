# Generated by Django 3.2 on 2022-02-13 07:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department_name', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Department',
            },
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('bedroom', models.IntegerField(default=1)),
                ('bathroom', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='StudentInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=200)),
                ('id_no', models.BigIntegerField()),
                ('age', models.IntegerField()),
                ('cgpa', models.DecimalField(decimal_places=2, default=0.0, max_digits=2)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.department')),
            ],
        ),
    ]
