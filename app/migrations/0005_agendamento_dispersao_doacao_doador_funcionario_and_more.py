# Generated by Django 4.1.10 on 2023-09-27 01:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0004_alter_lembrete_descricao'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agendamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DIA_DISPONIVEL', models.CharField(max_length=45)),
                ('DATA_HORA', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Dispersao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('QTD_BOLSA', models.CharField(max_length=45)),
                ('DATA', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Doacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DATA_HORA', models.DateTimeField()),
                ('COD_AGEN', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.agendamento')),
            ],
        ),
        migrations.CreateModel(
            name='Doador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NOME', models.CharField(max_length=100)),
                ('ENDERECO', models.CharField(max_length=200)),
                ('CPF', models.BigIntegerField()),
                ('TELEFONE', models.CharField(max_length=15)),
                ('DATA_NASCIMENTO', models.DateField()),
                ('PESO', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NOME', models.CharField(max_length=45)),
                ('CPF', models.BigIntegerField()),
                ('ENDERECO', models.CharField(max_length=210)),
                ('TELEFONE', models.CharField(max_length=15)),
                ('USUARIO', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CNPJ', models.CharField(max_length=45)),
                ('NOME', models.CharField(max_length=200)),
                ('ENDERECO', models.CharField(max_length=200)),
                ('TELEFONE', models.CharField(max_length=15)),
                ('EMAIL', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='TipoSangue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TIPO', models.CharField(max_length=45)),
                ('QUANTIDADE', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Lembrete',
        ),
        migrations.AddField(
            model_name='doador',
            name='COD_TIPOSANG',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.tiposangue'),
        ),
        migrations.AddField(
            model_name='doacao',
            name='COD_FUNC',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.funcionario'),
        ),
        migrations.AddField(
            model_name='dispersao',
            name='COD_FUNC',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.funcionario'),
        ),
        migrations.AddField(
            model_name='dispersao',
            name='COD_HOSPITAL',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.hospital'),
        ),
        migrations.AddField(
            model_name='dispersao',
            name='COD_TIPOSANG',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.tiposangue'),
        ),
        migrations.AddField(
            model_name='agendamento',
            name='COD_DOADOR',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.doador'),
        ),
    ]
