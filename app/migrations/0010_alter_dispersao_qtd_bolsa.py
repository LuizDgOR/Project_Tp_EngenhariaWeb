# Generated by Django 4.1.10 on 2023-10-29 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_alter_dispersao_qtd_bolsa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dispersao',
            name='qtd_bolsa',
            field=models.IntegerField(),
        ),
    ]
