# Generated by Django 3.1.7 on 2023-07-21 14:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('postmedia', '0006_auto_20230721_1601'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post_details',
            old_name='post_img',
            new_name='postImg',
        ),
        migrations.RenameField(
            model_name='post_details',
            old_name='time_posted',
            new_name='timePosted',
        ),
    ]
