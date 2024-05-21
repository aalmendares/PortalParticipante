# Generated by Django 5.0.6 on 2024-05-13 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='solicitud_separaciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numeroSolicitud', models.IntegerField()),
                ('hojaTrabajo', models.IntegerField()),
                ('cdrp', models.CharField(max_length=50)),
                ('dni', models.CharField(max_length=50)),
                ('nombreSistema', models.CharField(max_length=100)),
                ('nombreCorrecto', models.CharField(max_length=100)),
                ('ramo', models.CharField(max_length=50)),
                ('Campo', models.DateField()),
                ('dependencia', models.CharField(max_length=50)),
                ('fechaRo', models.DateField()),
                ('fechaAnalisis', models.DateField()),
                ('cotizacionesMacot', models.DecimalField(decimal_places=2, max_digits=10)),
                ('rebajas', models.DecimalField(decimal_places=2, max_digits=10)),
                ('montoBeneficios', models.DecimalField(decimal_places=2, max_digits=10)),
                ('montoResumen', models.DecimalField(decimal_places=2, max_digits=10)),
                ('diferencia', models.DecimalField(decimal_places=2, max_digits=10)),
                ('montoRo', models.DecimalField(decimal_places=2, max_digits=10)),
                ('interesAlRo', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cotDespuesRoAl12052014', models.DecimalField(decimal_places=2, max_digits=10)),
                ('intDespuesRoAl12052014', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cot13052014Delante', models.DecimalField(decimal_places=2, max_digits=10)),
                ('interesRebajas', models.DecimalField(decimal_places=2, max_digits=10)),
                ('tasaMes', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                'db_table': 'solicitud_separaciones',
                'managed': False,
            },
        ),
    ]
