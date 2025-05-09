# Generated by Django 5.2.1 on 2025-05-07 21:01

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cuentas', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cuenta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('saldo', models.DecimalField(decimal_places=2, default=0.0, max_digits=12)),
                ('moneda', models.CharField(default='PEN', max_length=3)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cuentas', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Cuentas',
            },
        ),
        migrations.AddField(
            model_name='transaccion',
            name='cuenta',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='transacciones', to='cuentas.cuenta'),
        ),
        migrations.CreateModel(
            name='Presupuesto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monto_presupuestado', models.DecimalField(decimal_places=2, max_digits=10)),
                ('periodo_inicio', models.DateField()),
                ('periodo_fin', models.DateField()),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='presupuestos', to='cuentas.categoria')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='presupuestos', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Presupuestos',
                'unique_together': {('usuario', 'categoria', 'periodo_inicio', 'periodo_fin')},
            },
        ),
    ]
