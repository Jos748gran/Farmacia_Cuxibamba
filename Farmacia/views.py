from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import PasswordChangeView
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy

from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.views.decorators.csrf import csrf_protect

from Farmacia.forms import UsuarioForm



@login_required
def home_view(request):
    return render(request, 'home.html')
@login_required
def management_system_view(request):
    return render(request, 'management_system.html')

def root(request):
    return redirect('home')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('management_system')
            else:
                return HttpResponse('Invalid login credentials')
        else:
            return HttpResponse('Invalid form data')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

def registrar_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = UsuarioForm()
    return render(request, 'registrar_usuario.html', {'form': form})

def success(request):
    return render(request, 'success.html')

def cliente(request):
    return render(request, 'cliente.html')

def empleado(request):
    return render(request, 'empleado.html')

def logout_view(request):
    logout(request)
    return redirect('login')

class CustomPasswordChangeView(PasswordChangeView):
    template_name = 'registration/password_change_form.html'
    success_url = reverse_lazy('password_change_done')



# Farmacia/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Medicamento, Usuario
from .forms import MedicamentoForm

def medicamento_list(request):
    medicamentos = Medicamento.objects.all()
    return render(request, 'medicamentos/medicamento_list.html', {'medicamentos': medicamentos})

def medicamento_create(request):
    if request.method == 'POST':
        form = MedicamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('medicamento_list')
    else:
        form = MedicamentoForm()
    return render(request, 'medicamentos/medicamento_form.html', {'form': form})

def medicamento_update(request, pk):
    medicamento = get_object_or_404(Medicamento, pk=pk)
    if request.method == 'POST':
        form = MedicamentoForm(request.POST, instance=medicamento)
        if form.is_valid():
            form.save()
            return redirect('medicamento_list')
    else:
        form = MedicamentoForm(instance=medicamento)
    return render(request, 'medicamentos/medicamento_form.html', {'form': form})

def medicamento_delete(request, pk):
    medicamento = get_object_or_404(Medicamento, pk=pk)
    if request.method == 'POST':
        medicamento.delete()
        return redirect('medicamento_list')
    return render(request, 'medicamentos/medicamento_confirm_delete.html', {'medicamento': medicamento})
# Farmacia/views.py
from .models import Cliente
from .forms import ClienteForm

def cliente_list(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes/cliente_list.html', {'clientes': clientes})

def cliente_create(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cliente_list')
    else:
        form = ClienteForm()
    return render(request, 'clientes/cliente_form.html', {'form': form})

def cliente_update(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('cliente_list')
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'clientes/cliente_form.html', {'form': form})

def cliente_delete(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        cliente.delete()
        return redirect('cliente_list')
    return render(request, 'clientes/cliente_confirm_delete.html', {'cliente': cliente})

# Farmacia/views.py
from .models import Dirección
from .forms import DirecciónForm

def direccion_list(request):
    direcciones = Dirección.objects.all()
    return render(request, 'direcciones/direccion_list.html', {'direcciones': direcciones})

def direccion_create(request):
    if request.method == 'POST':
        form = DirecciónForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('direccion_list')
    else:
        form = DirecciónForm()
    return render(request, 'direcciones/direccion_form.html', {'form': form})

def direccion_update(request, pk):
    direccion = get_object_or_404(Dirección, pk=pk)
    if request.method == 'POST':
        form = DirecciónForm(request.POST, instance=direccion)
        if form.is_valid():
            form.save()
            return redirect('direccion_list')
    else:
        form = DirecciónForm(instance=direccion)
    return render(request, 'direcciones/direccion_form.html', {'form': form})

def direccion_delete(request, pk):
    direccion = get_object_or_404(Dirección, pk=pk)
    if request.method == 'POST':
        direccion.delete()
        return redirect('direccion_list')
    return render(request, 'direcciones/direccion_confirm_delete.html', {'direccion': direccion})
# Farmacia/views.py
from .models import Farmacia
from .forms import FarmaciaForm

def farmacia_list(request):
    farmacias = Farmacia.objects.all()
    return render(request, 'farmacias/farmacia_list.html', {'farmacias': farmacias})

def farmacia_create(request):
    if request.method == 'POST':
        form = FarmaciaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('farmacia_list')
    else:
        form = FarmaciaForm()
    return render(request, 'farmacias/farmacia_form.html', {'form': form})

def farmacia_update(request, pk):
    farmacia = get_object_or_404(Farmacia, pk=pk)
    if request.method == 'POST':
        form = FarmaciaForm(request.POST, instance=farmacia)
        if form.is_valid():
            form.save()
            return redirect('farmacia_list')
    else:
        form = FarmaciaForm(instance=farmacia)
    return render(request, 'farmacias/farmacia_form.html', {'form': form})

def farmacia_delete(request, pk):
    farmacia = get_object_or_404(Farmacia, pk=pk)
    if request.method == 'POST':
        farmacia.delete()
        return redirect('farmacia_list')
    return render(request, 'farmacias/farmacia_confirm_delete.html', {'farmacia': farmacia})
# Farmacia/views.py
from .models import Sucursal
from .forms import SucursalForm

def sucursal_list(request):
    sucursales = Sucursal.objects.all()
    return render(request, 'sucursales/sucursal_list.html', {'sucursales': sucursales})

def sucursal_create(request):
    if request.method == 'POST':
        form = SucursalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sucursal_list')
    else:
        form = SucursalForm()
    return render(request, 'sucursales/sucursal_form.html', {'form': form})

def sucursal_update(request, pk):
    sucursal = get_object_or_404(Sucursal, pk=pk)
    if request.method == 'POST':
        form = SucursalForm(request.POST, instance=sucursal)
        if form.is_valid():
            form.save()
            return redirect('sucursal_list')
    else:
        form = SucursalForm(instance=sucursal)
    return render(request, 'sucursales/sucursal_form.html', {'form': form})

def sucursal_delete(request, pk):
    sucursal = get_object_or_404(Sucursal, pk=pk)
    if request.method == 'POST':
        sucursal.delete()
        return redirect('sucursal_list')
    return render(request, 'sucursales/sucursal_confirm_delete.html', {'sucursal': sucursal})
# Farmacia/views.py
from .models import Administrativo
from .forms import AdministrativoForm

def administrativo_list(request):
    administrativos = Administrativo.objects.all()
    return render(request, 'administrativos/administrativo_list.html', {'administrativos': administrativos})

def administrativo_create(request):
    if request.method == 'POST':
        form = AdministrativoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('administrativo_list')
    else:
        form = AdministrativoForm()
    return render(request, 'administrativos/administrativo_form.html', {'form': form})

def administrativo_update(request, pk):
    administrativo = get_object_or_404(Administrativo, pk=pk)
    if request.method == 'POST':
        form = AdministrativoForm(request.POST, instance=administrativo)
        if form.is_valid():
            form.save()
            return redirect('administrativo_list')
    else:
        form = AdministrativoForm(instance=administrativo)
    return render(request, 'administrativos/administrativo_form.html', {'form': form})

def administrativo_delete(request, pk):
    administrativo = get_object_or_404(Administrativo, pk=pk)
    if request.method == 'POST':
        administrativo.delete()
        return redirect('administrativo_list')
    return render(request, 'administrativos/administrativo_confirm_delete.html', {'administrativo': administrativo})


# Farmacia/views.py
from .models import Venta
from .forms import VentaForm

def venta_list(request):
    ventas = Venta.objects.all()
    return render(request, 'ventas/venta_list.html', {'ventas': ventas})

def venta_create(request):
    if request.method == 'POST':
        form = VentaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('venta_list')
    else:
        form = VentaForm()
    return render(request, 'ventas/venta_form.html', {'form': form})

def venta_update(request, pk):
    venta = get_object_or_404(Venta, pk=pk)
    if request.method == 'POST':
        form = VentaForm(request.POST, instance=venta)
        if form.is_valid():
            form.save()
            return redirect('venta_list')
    else:
        form = VentaForm(instance=venta)
    return render(request, 'ventas/venta_form.html', {'form': form})

def venta_delete(request, pk):
    venta = get_object_or_404(Venta, pk=pk)
    if request.method == 'POST':
        venta.delete()
        return redirect('venta_list')
    return render(request, 'ventas/venta_confirm_delete.html', {'venta': venta})

# Farmacia/views.py
from .models import Inventario
from .forms import InventarioForm

def inventario_list(request):
    inventarios = Inventario.objects.all()
    return render(request, 'inventarios/inventario_list.html', {'inventarios': inventarios})

def inventario_create(request):
    if request.method == 'POST':
        form = InventarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inventario_list')
    else:
        form = InventarioForm()
    return render(request, 'inventarios/inventario_form.html', {'form': form})

def inventario_update(request, pk):
    inventario = get_object_or_404(Inventario, pk=pk)
    if request.method == 'POST':
        form = InventarioForm(request.POST, instance=inventario)
        if form.is_valid():
            form.save()
            return redirect('inventario_list')
    else:
        form = InventarioForm(instance=inventario)
    return render(request, 'inventarios/inventario_form.html', {'form': form})

def inventario_delete(request, pk):
    inventario = get_object_or_404(Inventario, pk=pk)
    if request.method == 'POST':
        inventario.delete()
        return redirect('inventario_list')
    return render(request, 'inventarios/inventario_confirm_delete.html', {'inventario': inventario})

# Farmacia/views.py
from .models import TransferenciaDeMedicamento
from .forms import TransferenciaDeMedicamentosForm

def transferencia_list(request):
    transferencias = TransferenciaDeMedicamento.objects.all()
    return render(request, 'transferencias/transferencia_list.html', {'transferencias': transferencias})

def transferencia_create(request):
    if request.method == 'POST':
        form = TransferenciaDeMedicamentosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('transferencia_list')
    else:
        form = TransferenciaDeMedicamentosForm()
    return render(request, 'transferencias/transferencia_form.html', {'form': form})

def transferencia_update(request, pk):
    transferencia = get_object_or_404(TransferenciaDeMedicamento, pk=pk)
    if request.method == 'POST':
        form = TransferenciaDeMedicamentosForm(request.POST, instance=transferencia)
        if form.is_valid():
            form.save()
            return redirect('transferencia_list')
    else:
        form = TransferenciaDeMedicamentosForm(instance=transferencia)
    return render(request, 'transferencias/transferencia_form.html', {'form': form})

def transferencia_delete(request, pk):
    transferencia = get_object_or_404(TransferenciaDeMedicamento, pk=pk)
    if request.method == 'POST':
        transferencia.delete()
        return redirect('transferencia_list')
    return render(request, 'transferencias/transferencia_confirm_delete.html', {'transferencia': transferencia})

# Farmacia/views.py
from .models import DetalleVenta
from .forms import DetalleVentaForm

def detalle_venta_list(request):
    detalles_venta = DetalleVenta.objects.all()
    return render(request, 'detalles_venta/detalle_venta_list.html', {'detalles_venta': detalles_venta})

def detalle_venta_create(request):
    if request.method == 'POST':
        form = DetalleVentaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('detalle_venta_list')
    else:
        form = DetalleVentaForm()
    return render(request, 'detalles_venta/detalle_venta_form.html', {'form': form})

def detalle_venta_update(request, pk):
    detalle_venta = get_object_or_404(DetalleVenta, pk=pk)
    if request.method == 'POST':
        form = DetalleVentaForm(request.POST, instance=detalle_venta)
        if form.is_valid():
            form.save()
            return redirect('detalle_venta_list')
    else:
        form = DetalleVentaForm(instance=detalle_venta)
    return render(request, 'detalles_venta/detalle_venta_form.html', {'form': form})

def detalle_venta_delete(request, pk):
    detalle_venta = get_object_or_404(DetalleVenta, pk=pk)
    if request.method == 'POST':
        detalle_venta.delete()
        return redirect('detalle_venta_list')
    return render(request, 'detalles_venta/detalle_venta_confirm_delete.html', {'detalle_venta': detalle_venta})

def usuario_list(request):
    usuarios = Usuario.objects.all()
    return render(request, 'usuarios/usuario_list.html', {'usuarios': usuarios})

def usuario_create(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('usuario_list')
    else:
        form = UsuarioForm()
    return render(request, 'usuarios/usuario_form.html', {'form': form})

def usuario_update(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('usuario_list')
    else:
        form = UsuarioForm(instance=usuario)
    return render(request, 'usuarios/usuario_form.html', {'form': form})

def usuario_delete(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    if request.method == 'POST':
        usuario.delete()
        return redirect('usuario_list')
    return render(request, 'usuarios/usuario_confirm_delete.html', {'usuario': usuario})



