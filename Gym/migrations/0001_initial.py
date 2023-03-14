# Generated by Django 4.1.7 on 2023-03-14 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bebida',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_bebida', models.CharField(max_length=20)),
                ('precio_bebida', models.IntegerField()),
                ('marca_bebida', models.CharField(max_length=20)),
                ('litros_bebida', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Clase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_clase', models.CharField(max_length=20)),
                ('precio_clase', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Entrenador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_entrenador', models.CharField(max_length=20)),
                ('clase_entrenador', models.CharField(max_length=10)),
            ],
        ),
    ]