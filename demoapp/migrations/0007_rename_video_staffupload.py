# Generated by Django 4.0 on 2022-05-15 15:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demoapp', '0006_delete_staffupload'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Video',
            new_name='StaffUpload',
        ),
    ]
