# Generated by Django 4.2.4 on 2023-09-23 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('owl_blue_app', '0006_alter_abecedario_linkimg_alter_actividades_videos_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abecedario',
            name='linkimg',
            field=models.CharField(max_length=1000, unique=True),
        ),
        migrations.AlterField(
            model_name='explicaciones',
            name='img',
            field=models.CharField(max_length=1000, unique=True),
        ),
        migrations.AlterField(
            model_name='explicaciones',
            name='vid',
            field=models.CharField(max_length=1000, unique=True),
        ),
    ]
