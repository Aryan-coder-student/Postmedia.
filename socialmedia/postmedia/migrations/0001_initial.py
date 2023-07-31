# Generated by Django 3.1.7 on 2023-07-20 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='post_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('description', models.TextField(max_length=100000)),
                ('post_img', models.ImageField(upload_to='user_post_images/')),
                ('likes', models.IntegerField()),
                ('dislikes', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='user_fav_post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]