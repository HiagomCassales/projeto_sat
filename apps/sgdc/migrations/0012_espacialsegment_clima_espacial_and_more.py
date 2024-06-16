# Generated by Django 5.0.6 on 2024-06-16 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sgdc', '0011_remove_espacialsegment_clima_espacial_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='espacialsegment',
            name='clima_espacial',
            field=models.CharField(choices=[('NORMAL', 'Normal'), ('OK', 'OK'), ('WARN', 'Warning'), ('CRIT', 'Critical')], default='OK', max_length=100, verbose_name='Clima Espacial'),
        ),
        migrations.AddField(
            model_name='espacialsegment',
            name='descricao_operacao',
            field=models.TextField(blank=True, null=True, verbose_name='Descrição da Operação'),
        ),
        migrations.AddField(
            model_name='espacialsegment',
            name='gcn_tcr_brasilia',
            field=models.CharField(choices=[('NORMAL', 'Normal'), ('OK', 'OK'), ('WARN', 'Warning'), ('CRIT', 'Critical')], default='OK', max_length=100, verbose_name='GCN/TCR Brasília'),
        ),
        migrations.AddField(
            model_name='espacialsegment',
            name='gcn_tcr_rio',
            field=models.CharField(choices=[('NORMAL', 'Normal'), ('OK', 'OK'), ('WARN', 'Warning'), ('CRIT', 'Critical')], default='OK', max_length=100, verbose_name='GCN/TCR Rio de Janeiro'),
        ),
        migrations.AddField(
            model_name='espacialsegment',
            name='infra_critica_brasilia',
            field=models.CharField(choices=[('NORMAL', 'Normal'), ('OK', 'OK'), ('WARN', 'Warning'), ('CRIT', 'Critical')], default='OK', max_length=100, verbose_name='Infra Crítica Brasília'),
        ),
        migrations.AddField(
            model_name='espacialsegment',
            name='infra_critica_rio',
            field=models.CharField(choices=[('NORMAL', 'Normal'), ('OK', 'OK'), ('WARN', 'Warning'), ('CRIT', 'Critical')], default='OK', max_length=100, verbose_name='Infra Crítica Rio de Janeiro'),
        ),
        migrations.AddField(
            model_name='espacialsegment',
            name='ssa_sda',
            field=models.CharField(choices=[('NORMAL', 'Normal'), ('OK', 'OK'), ('WARN', 'Warning'), ('CRIT', 'Critical')], default='OK', max_length=100, verbose_name='SSA/SDA'),
        ),
    ]