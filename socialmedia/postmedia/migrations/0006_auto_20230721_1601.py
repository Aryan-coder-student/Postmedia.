# Generated by Django 3.1.7 on 2023-07-21 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postmedia', '0005_post_details'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post_details',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]
