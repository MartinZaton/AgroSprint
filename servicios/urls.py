from django.urls import path
from django.contrib.auth import views as auth_views  # ← Importamos las vistas nativas
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('servicios/', views.lista_servicios, name='lista_servicios'),
    path('servicio/<int:pk>/', views.detalle_servicio, name='detalle_servicio'),
    path('servicio/nuevo/', views.crear_servicio, name='crear_servicio'),
    path('evento/nuevo/', views.crear_evento, name='crear_evento'),
    path('registro/', views.registro_usuario, name='registro_usuario'),
    path('login/', auth_views.LoginView.as_view(template_name='servicios/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]