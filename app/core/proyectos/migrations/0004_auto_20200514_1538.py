# Generated by Django 2.2.12 on 2020-05-14 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyectos', '0003_auto_20200513_1750'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyectos',
            name='imgProy',
            field=models.ImageField(default='proyecto.png', upload_to='perfiles/img', verbose_name='Foto del Proyecto'),
        ),
    ]
