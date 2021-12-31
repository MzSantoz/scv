# Generated by Django 4.0 on 2021-12-31 17:15

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('razao_social', models.CharField(max_length=255, verbose_name='Razão Social')),
                ('indicado', models.CharField(choices=[('S', 'Sim'), ('N', 'Não')], default='N', max_length=1, verbose_name='Indicação ?')),
                ('data_da_visita', models.DateField(verbose_name='Data da Visita')),
                ('atividade', models.TextField(blank=True, max_length=200, null=True, verbose_name='Atividade')),
                ('endereco', models.TextField(blank=True, max_length=255, null=True, verbose_name='Endereço'))],
            options={
                'verbose_name': 'Empresa',
            },
        ),
    ]
