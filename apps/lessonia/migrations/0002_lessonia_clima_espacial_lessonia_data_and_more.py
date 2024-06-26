# Generated by Django 5.0.6 on 2024-06-19 23:38

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lessonia', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lessonia',
            name='clima_espacial',
            field=models.CharField(choices=[('NORMAL', 'Normal'), ('OK', 'OK'), ('WARN', 'Warning'), ('CRIT', 'Critical')], default='OK', max_length=100, verbose_name='Clima Espacial'),
        ),
        migrations.AddField(
            model_name='lessonia',
            name='data',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Data'),
        ),
        migrations.AddField(
            model_name='lessonia',
            name='descricao_operacao',
            field=models.TextField(blank=True, null=True, verbose_name='Descrição da Operação'),
        ),
        migrations.AddField(
            model_name='lessonia',
            name='gcn_tcr_brasilia',
            field=models.CharField(choices=[('NORMAL', 'Normal'), ('OK', 'OK'), ('WARN', 'Warning'), ('CRIT', 'Critical')], default='OK', max_length=100, verbose_name='GCN/TCR Brasília'),
        ),
        migrations.AddField(
            model_name='lessonia',
            name='gcn_tcr_rio',
            field=models.CharField(choices=[('NORMAL', 'Normal'), ('OK', 'OK'), ('WARN', 'Warning'), ('CRIT', 'Critical')], default='OK', max_length=100, verbose_name='GCN/TCR Rio de Janeiro'),
        ),
        migrations.AddField(
            model_name='lessonia',
            name='infra_critica_brasilia',
            field=models.CharField(choices=[('NORMAL', 'Normal'), ('OK', 'OK'), ('WARN', 'Warning'), ('CRIT', 'Critical')], default='OK', max_length=100, verbose_name='Infra Crítica Brasília'),
        ),
        migrations.AddField(
            model_name='lessonia',
            name='infra_critica_rio',
            field=models.CharField(choices=[('NORMAL', 'Normal'), ('OK', 'OK'), ('WARN', 'Warning'), ('CRIT', 'Critical')], default='OK', max_length=100, verbose_name='Infra Crítica Rio de Janeiro'),
        ),
        migrations.AddField(
            model_name='lessonia',
            name='ssa_sda',
            field=models.CharField(choices=[('NORMAL', 'Normal'), ('OK', 'OK'), ('WARN', 'Warning'), ('CRIT', 'Critical')], default='OK', max_length=100, verbose_name='SSA/SDA'),
        ),
        migrations.AlterUniqueTogether(
            name='lessonia',
            unique_together={('data',)},
        ),
    ]
