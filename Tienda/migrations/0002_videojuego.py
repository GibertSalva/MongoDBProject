# Generated by Django 3.2.9 on 2021-11-18 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tienda', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Videojuego',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publicadora_id', models.CharField(max_length=100)),
                ('game_id', models.CharField(max_length=100)),
                ('nombre', models.CharField(max_length=100)),
                ('tipo_juego', models.CharField(max_length=100)),
                ('release_date', models.CharField(max_length=100)),
                ('Espacio', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
