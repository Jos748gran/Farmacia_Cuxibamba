
from django import forms
from Farmacia.models import Usuario, Dirección


class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['cedula', 'nombre', 'teléfono', 'rol', 'nombre_usuario',]
        widgets = {
            'password': forms.PasswordInput(),
        }



from .models import Medicamento

class MedicamentoForm(forms.ModelForm):
    class Meta:
        model = Medicamento
        fields = ['nombre_medicamento', 'descripcion', 'presentación']


from .models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['cedula', 'nombre', 'teléfono', 'dirección']

class DirecciónForm(forms.ModelForm):
    class Meta:
        model = Dirección
        fields = ['calle_principal', 'calle_secundaria', 'ciudad']




from .models import Farmacia

class FarmaciaForm(forms.ModelForm):
    class Meta:
        model = Farmacia
        fields = ['nombre']



from .models import Sucursal

class SucursalForm(forms.ModelForm):
    class Meta:
        model = Sucursal
        fields = ['nombre', 'dirección', 'teléfono', 'farmacia']



from .models import Administrativo

class AdministrativoForm(forms.ModelForm):
    class Meta:
        model = Administrativo
        fields = ['cedula', 'nombre', 'teléfono', 'identificación', 'sueldo', 'sucursal', 'cargo', 'horario']


from .models import Venta

class VentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = ['cliente', 'sucursal', 'tipo_pago', 'fecha', 'total']



from .models import Inventario

class InventarioForm(forms.ModelForm):
    class Meta:
        model = Inventario
        fields = ['sucursal', 'medicamento', 'cantidad_inventario']



from .models import TransferenciaDeMedicamentos

class TransferenciaDeMedicamentosForm(forms.ModelForm):
    class Meta:
        model = TransferenciaDeMedicamentos
        fields = ['sucursal_origen', 'sucursal_destino', 'medicamento', 'cantidad_transferencia', 'fecha']


from .models import DetalleVenta

class DetalleVentaForm(forms.ModelForm):
    class Meta:
        model = DetalleVenta
        fields = ['venta', 'medicamento', 'cantidad_medicamento', 'precio']
