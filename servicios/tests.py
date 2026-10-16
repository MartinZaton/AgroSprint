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

    def test_portada_explicativa_responde(self):
        response = self.client.get(reverse('inicio'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '¿Qué es AgroSprint?')
        self.assertContains(response, '¿Cómo se usa?')
        self.assertContains(response, 'Crear cuenta gratis')
        self.assertContains(response, reverse('registro_usuario'))
        self.assertContains(response, reverse('lista_servicios'))
        self.assertEqual(response.content.decode().count('agrosprint-background.jpg'), 1)

    def test_registro_muestra_campos_legibles_y_estilizados(self):
        response = self.client.get(reverse('registro_usuario'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Nombre de usuario')
        self.assertContains(response, 'Confirmar contraseña')
        self.assertContains(response, 'w-full px-4 py-3 border')
        self.assertContains(response, 'Iniciá sesión')

    def test_lista_servicios_responde(self):
        response = self.client.get(reverse('lista_servicios'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Servicios Agropecuarios')

    def test_paginas_usan_el_fondo_compartido(self):
        self.client.force_login(self.user)
        urls = [
            reverse('login'),
            reverse('registro_usuario'),
            reverse('lista_servicios'),
            reverse('crear_servicio'),
            reverse('crear_evento'),
            reverse('detalle_servicio', args=[self._crear_servicio().pk]),
        ]

        for url in urls:
            with self.subTest(url=url):
                response = self.client.get(url)
                self.assertEqual(response.status_code, 200)
                self.assertContains(response, 'agrosprint-background.jpg')

    def _crear_servicio(self):
        return ServicioAgro.objects.create(
            usuario=self.user,
            tipo_oferta=ServicioAgro.TipoOferta.PRESTADOR,
            titulo='Servicio de prueba',
            categoria=ServicioAgro.Categoria.SIEMBRA,
            descripcion='Descripción de prueba.',
            ubicacion=ServicioAgro.Ubicacion.BUENOS_AIRES,
            contacto='5491123456789',
        )

    def test_usuario_puede_publicar_servicio(self):
        self.client.force_login(self.user)
        response = self.client.post(
            reverse('crear_servicio'),
            {
                'tipo_oferta': ServicioAgro.TipoOferta.PRESTADOR,
                'titulo': 'Transporte de maquinaria',
                'categoria': ServicioAgro.Categoria.TRANSPORTE,
                'descripcion': 'Traslado de maquinaria agrícola.',
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
