from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import EventoForm, RegistroUsuarioForm, ServicioForm
from .models import ServicioAgro


def inicio(request):
    return render(request, 'servicios/inicio.html')


def lista_servicios(request):
    servicios = ServicioAgro.objects.select_related('usuario')
    tipo = request.GET.get('tipo', '')
    categoria = request.GET.get('categoria', '')
    ubicacion = request.GET.get('ubicacion', '')

    if tipo in ServicioAgro.TipoOferta.values:
        servicios = servicios.filter(tipo_oferta=tipo)
    if categoria in ServicioAgro.Categoria.values:
        servicios = servicios.filter(categoria=categoria)
    if ubicacion in ServicioAgro.Ubicacion.values:
        servicios = servicios.filter(ubicacion=ubicacion)

    return render(
        request,
        'servicios/lista.html',
        {
            'servicios': servicios,
            'tipos': ServicioAgro.TipoOferta.choices,
            'categorias': ServicioAgro.Categoria.choices,
            'zonas': ServicioAgro.Ubicacion.choices,
            'tipo_seleccionado': tipo,
            'cat_seleccionada': categoria,
            'ub_seleccionada': ubicacion,
        },
    )


def detalle_servicio(request, pk):
    servicio = get_object_or_404(
        ServicioAgro.objects.select_related('usuario'),
        pk=pk,
    )
    return render(request, 'servicios/detalle.html', {'servicio': servicio})


@login_required
def crear_servicio(request):
    form = ServicioForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        servicio = form.save(commit=False)
        servicio.usuario = request.user
        servicio.save()
        return redirect('detalle_servicio', pk=servicio.pk)
    return render(request, 'servicios/crear_servicio.html', {'form': form})


@login_required
def crear_evento(request):
    form = EventoForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        evento = form.save(commit=False)
        evento.usuario = request.user
        evento.save()
        return redirect('lista_servicios')
    return render(request, 'servicios/crear_evento.html', {'form': form})


def registro_usuario(request):
    form = RegistroUsuarioForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = form.save()
        login(request, user, backend='django.contrib.auth.backends.ModelBackend')
        return redirect('lista_servicios')
    return render(request, 'servicios/registro.html', {'form': form})
