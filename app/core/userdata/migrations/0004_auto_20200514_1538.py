# Generated by Django 2.2.12 on 2020-05-14 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userdata', '0003_auto_20200513_1743'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datosuser',
            name='fotoUser',
            field=models.ImageField(default='user.png', upload_to='perfiles/img', verbose_name='Foto de perfil'),
        ),
    ]
