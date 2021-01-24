# Generated by Django 3.1.2 on 2021-01-23 09:29

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0003_auto_20210123_1455'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='liked_by',
            field=models.ManyToManyField(related_name='liked_post', to=settings.AUTH_USER_MODEL),
        ),
    ]