# Generated by Django 5.0.6 on 2024-06-16 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sgdc', '0008_alter_espacialsegment_prox_manobra'),
    ]

    operations = [
        migrations.AddField(
            model_name='espacialsegment',
            name='observacoes',
            field=models.TextField(blank=True, null=True, verbose_name='Observações'),
        ),
        migrations.AlterField(
            model_name='espacialsegment',
            name='alerta_conjuncao',
            field=models.CharField(choices=[('NORMAL', 'Normal'), ('OK', 'OK'), ('WARN', 'Warning'), ('CRIT', 'Critical')], max_length=100),
        ),
        migrations.AlterField(
            model_name='espacialsegment',
            name='campanha_ranging',
            field=models.CharField(choices=[('NORMAL', 'Normal'), ('OK', 'OK'), ('WARN', 'Warning'), ('CRIT', 'Critical')], max_length=100),
        ),
        migrations.AlterField(
            model_name='espacialsegment',
            name='cmc_brasilia',
            field=models.CharField(choices=[('NORMAL', 'Normal'), ('OK', 'OK'), ('WARN', 'Warning'), ('CRIT', 'Critical')], default='OK', max_length=100, verbose_name='CMC-x Brasília'),
        ),
        migrations.AlterField(
            model_name='espacialsegment',
            name='cmc_rio',
            field=models.CharField(choices=[('NORMAL', 'Normal'), ('OK', 'OK'), ('WARN', 'Warning'), ('CRIT', 'Critical')], default='OK', max_length=100, verbose_name='CMC-x Rio'),
        ),
        migrations.AlterField(
            model_name='espacialsegment',
            name='plataforma_saude',
            field=models.CharField(choices=[('NORMAL', 'Normal'), ('OK', 'OK'), ('WARN', 'Warning'), ('CRIT', 'Critical')], max_length=10),
        ),
        migrations.AlterField(
            model_name='espacialsegment',
            name='proc_executados',
            field=models.CharField(choices=[('NORMAL', 'Normal'), ('OK', 'OK'), ('WARN', 'Warning'), ('CRIT', 'Critical')], max_length=100),
        ),
        migrations.AlterField(
            model_name='espacialsegment',
            name='qualidade_enlaces',
            field=models.CharField(choices=[('NORMAL', 'Normal'), ('OK', 'OK'), ('WARN', 'Warning'), ('CRIT', 'Critical')], default='OK', max_length=100, verbose_name='Qualidade dos Enlaces'),
        ),
        migrations.AlterField(
            model_name='espacialsegment',
            name='smc_brasilia',
            field=models.CharField(choices=[('NORMAL', 'Normal'), ('OK', 'OK'), ('WARN', 'Warning'), ('CRIT', 'Critical')], default='OK', max_length=100, verbose_name='SMC Brasília'),
        ),
        migrations.AlterField(
            model_name='espacialsegment',
            name='smc_rio',
            field=models.CharField(choices=[('NORMAL', 'Normal'), ('OK', 'OK'), ('WARN', 'Warning'), ('CRIT', 'Critical')], default='OK', max_length=100, verbose_name='SMC Rio'),
        ),
        migrations.AlterField(
            model_name='espacialsegment',
            name='tcr_brasilia',
            field=models.CharField(choices=[('NORMAL', 'Normal'), ('OK', 'OK'), ('WARN', 'Warning'), ('CRIT', 'Critical')], default='OK', max_length=100, verbose_name='Antena (TCR) Brasília'),
        ),
        migrations.AlterField(
            model_name='espacialsegment',
            name='tcr_rio',
            field=models.CharField(choices=[('NORMAL', 'Normal'), ('OK', 'OK'), ('WARN', 'Warning'), ('CRIT', 'Critical')], default='OK', max_length=100, verbose_name='Antena (TCR) Rio'),
        ),
    ]
