# Generated by Django 4.1 on 2022-09-16 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theme', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BranchModel',
            fields=[
                ('Branch_code', models.CharField(max_length=10, primary_key=True, serialize=False, unique=True)),
                ('Add1', models.TextField(max_length=100)),
                ('Add2', models.TextField(max_length=100)),
                ('City', models.CharField(max_length=20)),
                ('Telephone', models.CharField(max_length=10)),
            ],
        ),
    ]
