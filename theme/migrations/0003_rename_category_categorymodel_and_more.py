# Generated by Django 4.1 on 2022-09-02 08:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('theme', '0002_category'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Category',
            new_name='CategoryModel',
        ),
        migrations.RenameField(
            model_name='categorymodel',
            old_name='desciption',
            new_name='description',
        ),
    ]
