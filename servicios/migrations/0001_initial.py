import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='EventoAgro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=120)),
                ('descripcion', models.TextField()),
                ('fecha', models.DateTimeField()),
                ('ubicacion', models.CharField(max_length=120)),
                (
                    'usuario',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='eventos_agro',
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                'verbose_name': 'evento agropecuario',
                'verbose_name_plural': 'eventos agropecuarios',
                'ordering': ['fecha'],
            },
        ),
        migrations.CreateModel(
            name='ServicioAgro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                (
                    'tipo_oferta',
                    models.CharField(
                        choices=[('PRESTADOR', 'Ofrezco'), ('BUSCO', 'Busco')],
                        max_length=10,
                    ),
                ),
                ('titulo', models.CharField(max_length=120)),
                (
                    'categoria',
                    models.CharField(
                        choices=[
                            ('MAQUINARIA', 'Maquinaria'),
                            ('SIEMBRA', 'Siembra'),
                            ('COSECHA', 'Cosecha'),
                            ('GANADERIA', 'Ganadería'),
                            ('ASESORIA', 'Asesoría'),
                            ('INSUMOS', 'Insumos'),
                            ('OTROS', 'Otros'),
                        ],
                        max_length=20,
                    ),
                ),
                ('descripcion', models.TextField()),
                (
                    'ubicacion',
                    models.CharField(
                        choices=[
                            ('Buenos Aires', 'Buenos Aires'),
                            ('Ciudad Autónoma de Buenos Aires', 'Ciudad Autónoma de Buenos Aires'),
                            ('Catamarca', 'Catamarca'),
                            ('Chaco', 'Chaco'),
                            ('Chubut', 'Chubut'),
                            ('Córdoba', 'Córdoba'),
                            ('Corrientes', 'Corrientes'),
                            ('Entre Ríos', 'Entre Ríos'),
                            ('Formosa', 'Formosa'),
                            ('Jujuy', 'Jujuy'),
                            ('La Pampa', 'La Pampa'),
                            ('La Rioja', 'La Rioja'),
                            ('Mendoza', 'Mendoza'),
                            ('Misiones', 'Misiones'),
                            ('Neuquén', 'Neuquén'),
                            ('Río Negro', 'Río Negro'),
                            ('Salta', 'Salta'),
                            ('San Juan', 'San Juan'),
                            ('San Luis', 'San Luis'),
                            ('Santa Cruz', 'Santa Cruz'),
                            ('Santa Fe', 'Santa Fe'),
                            ('Santiago del Estero', 'Santiago del Estero'),
                            ('Tierra del Fuego', 'Tierra del Fuego'),
                            ('Tucumán', 'Tucumán'),
                        ],
                        max_length=40,
                    ),
                ),
                ('contacto', models.CharField(max_length=20)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                (
                    'usuario',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='servicios_agro',
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                'verbose_name': 'servicio agropecuario',
                'verbose_name_plural': 'servicios agropecuarios',
                'ordering': ['-fecha_creacion'],
            },
        ),
    ]
