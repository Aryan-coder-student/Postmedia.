# Generated by Django 3.1.7 on 2023-07-20 17:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('postmedia', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='user_profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_user', models.IntegerField()),
                ('bio', models.TextField(max_length=2000)),
                ('prof_img', models.ImageField(default='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSsUNceR8jbqHa2R3491RxiE8Nmcy8PHiFLTfF_OQ6xng&s', upload_to='user_profile/')),
                ('status', models.CharField(max_length=2000)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='post_details',
        ),
        migrations.DeleteModel(
            name='user_fav_post',
        ),
    ]
