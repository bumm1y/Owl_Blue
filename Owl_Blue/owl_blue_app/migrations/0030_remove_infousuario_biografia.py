# Generated by Django 4.2.4 on 2023-11-28 17:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('owl_blue_app', '0029_alter_explicaciones_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='infousuario',
            name='biografia',
        ),
    ]
