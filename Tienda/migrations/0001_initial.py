# Generated by Django 3.2.9 on 2021-11-18 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cliente_id', models.CharField(max_length=100)),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=100)),
                ('fecha_nacimiento', models.CharField(max_length=100)),
                ('dni', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]