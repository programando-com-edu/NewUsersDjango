# Generated by Django 4.1.7 on 2023-03-12 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_cad_usuarios', '0002_rename_usuarios_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='idade',
            field=models.IntegerField(default=0),
        ),
    ]