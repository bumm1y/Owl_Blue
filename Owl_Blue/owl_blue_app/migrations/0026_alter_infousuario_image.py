# Generated by Django 4.2.4 on 2023-11-13 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('owl_blue_app', '0025_infousuario_biografia_infousuario_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infousuario',
            name='image',
            field=models.CharField(default='img/defaultuser.png', max_length=100),
        ),
    ]
