from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import ServicioAgro


class ServiciosViewsTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='productor',
            password='AgroSprint-test-password-2026',
        )

    def test_lista_servicios_responde(self):
        response = self.client.get(reverse('lista_servicios'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Servicios Agropecuarios')

    def test_usuario_puede_publicar_servicio(self):
        self.client.force_login(self.user)
        response = self.client.post(
            reverse('crear_servicio'),
            {
                'tipo_oferta': ServicioAgro.TipoOferta.PRESTADOR,
                'titulo': 'Servicio de siembra',
                'categoria': ServicioAgro.Categoria.SIEMBRA,
                'descripcion': 'Siembra de precisión.',
                'ubicacion': ServicioAgro.Ubicacion.BUENOS_AIRES,
                'contacto': '5491123456789',
            },
        )

        servicio = ServicioAgro.objects.get()
        self.assertRedirects(
            response,
            reverse('detalle_servicio', args=[servicio.pk]),
        )
        self.assertEqual(servicio.usuario, self.user)
