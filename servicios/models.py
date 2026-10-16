from django.conf import settings
from django.db import models


class ServicioAgro(models.Model):
    class TipoOferta(models.TextChoices):
        PRESTADOR = 'PRESTADOR', 'Ofrezco'
        BUSCO = 'BUSCO', 'Busco'

    class Categoria(models.TextChoices):
        MAQUINARIA = 'MAQUINARIA', 'Maquinaria'
        SIEMBRA = 'SIEMBRA', 'Siembra'
        COSECHA = 'COSECHA', 'Cosecha'
        GANADERIA = 'GANADERIA', 'Ganadería'
        ASESORIA = 'ASESORIA', 'Asesoría'
        INSUMOS = 'INSUMOS', 'Insumos'
        OTROS = 'OTROS', 'Otros'

    class Ubicacion(models.TextChoices):
        BUENOS_AIRES = 'Buenos Aires', 'Buenos Aires'
        CABA = 'Ciudad Autónoma de Buenos Aires', 'Ciudad Autónoma de Buenos Aires'
        CATAMARCA = 'Catamarca', 'Catamarca'
        CHACO = 'Chaco', 'Chaco'
        CHUBUT = 'Chubut', 'Chubut'
        CORDOBA = 'Córdoba', 'Córdoba'
        CORRIENTES = 'Corrientes', 'Corrientes'
        ENTRE_RIOS = 'Entre Ríos', 'Entre Ríos'
        FORMOSA = 'Formosa', 'Formosa'
        JUJUY = 'Jujuy', 'Jujuy'
        LA_PAMPA = 'La Pampa', 'La Pampa'
        LA_RIOJA = 'La Rioja', 'La Rioja'
        MENDOZA = 'Mendoza', 'Mendoza'
        MISIONES = 'Misiones', 'Misiones'
        NEUQUEN = 'Neuquén', 'Neuquén'
        RIO_NEGRO = 'Río Negro', 'Río Negro'
        SALTA = 'Salta', 'Salta'
        SAN_JUAN = 'San Juan', 'San Juan'
        SAN_LUIS = 'San Luis', 'San Luis'
        SANTA_CRUZ = 'Santa Cruz', 'Santa Cruz'
        SANTA_FE = 'Santa Fe', 'Santa Fe'
        SANTIAGO_DEL_ESTERO = 'Santiago del Estero', 'Santiago del Estero'
        TIERRA_DEL_FUEGO = 'Tierra del Fuego', 'Tierra del Fuego'
        TUCUMAN = 'Tucumán', 'Tucumán'

    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='servicios_agro',
    )
    tipo_oferta = models.CharField(max_length=10, choices=TipoOferta.choices)
    titulo = models.CharField(max_length=120)
    categoria = models.CharField(max_length=20, choices=Categoria.choices)
    descripcion = models.TextField()
    ubicacion = models.CharField(max_length=40, choices=Ubicacion.choices)
    contacto = models.CharField(max_length=20)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-fecha_creacion']
        verbose_name = 'servicio agropecuario'
        verbose_name_plural = 'servicios agropecuarios'

    def __str__(self):
        return self.titulo


class EventoAgro(models.Model):
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='eventos_agro',
    )
    titulo = models.CharField(max_length=120)
    descripcion = models.TextField()
    fecha = models.DateTimeField()
    ubicacion = models.CharField(max_length=120)

    class Meta:
        ordering = ['fecha']
        verbose_name = 'evento agropecuario'
        verbose_name_plural = 'eventos agropecuarios'

    def __str__(self):
        return self.titulo
