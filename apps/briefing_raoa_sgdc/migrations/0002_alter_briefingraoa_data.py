# Generated by Django 5.0.6 on 2024-06-23 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('briefing_raoa_sgdc', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='briefingraoa',
            name='data',
            field=models.DateField(),
        ),
    ]