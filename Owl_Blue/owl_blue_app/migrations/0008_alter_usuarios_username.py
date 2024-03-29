# Generated by Django 4.2.4 on 2023-09-23 18:56

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('owl_blue_app', '0007_alter_abecedario_linkimg_alter_explicaciones_img_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuarios',
            name='username',
            field=models.CharField(max_length=16, unique=True, validators=[django.core.validators.RegexValidator(code='usuario_inválido', message='El usuario ingresado no cumple lo requerido.', regex='^[a-Az-Z0-9]+$')]),
        ),
    ]
