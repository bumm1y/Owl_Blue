# Generated by Django 4.2.4 on 2023-10-17 00:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('owl_blue_app', '0013_usuarios_img_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuarios',
            name='img_user',
        ),
    ]
