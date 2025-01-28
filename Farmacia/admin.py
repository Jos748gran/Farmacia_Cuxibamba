from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ( 'nombre','dirección',)
    list_filter = ('nombre', 'dirección')
    search_fields = ('nombre', 'dirección')

@admin.register(Venta)
class VentaAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'sucursal', 'tipo_pago', 'total','fecha',)
    list_filter = ('cliente', 'sucursal', 'tipo_pago', 'total','fecha',)
    search_fields = ( 'tipo_pago', 'total','fecha',)

@admin.register(DetalleVenta)
class DetalleVentaAdmin(admin.ModelAdmin):
    list_display = ('cantidad_medicamento', 'precio')
    list_filter = ('cantidad_medicamento', 'precio')
    search_fields = ('cantidad_medicamento', 'precio')

class MedicamentoAdmin(admin.ModelAdmin):
    list_display = ( 'nombre_medicamento', 'descripcion', 'presentación')
    list_filter = ('nombre_medicamento', 'descripcion', 'presentación')
    search_fields = ('nombre_medicamento', 'descripcion', 'presentación')
admin.site.register(Medicamento, MedicamentoAdmin)


class InventarioAdmin(admin.ModelAdmin):
    list_display = ( 'sucursal','cantidad_inventario',)
    list_filter = ('sucursal','cantidad_inventario',)
    search_fields = ('cantidad_inventario',)
admin.site.register(Inventario, InventarioAdmin)

class TransferenciaDeMedicamentosAdmin(admin.ModelAdmin):
    list_display = ('medicamento','cantidad_transferencia', 'fecha')
    list_filter = ('medicamento','cantidad_transferencia', 'fecha')
    search_fields = ('cantidad_transferencia', 'fecha')
admin.site.register(TransferenciaDeMedicamentos, TransferenciaDeMedicamentosAdmin)


class SucursalAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'dirección', 'teléfono')
    list_filter = ('nombre', 'dirección', 'teléfono')
    search_fields = ('nombre', 'teléfono')
admin.site.register(Sucursal, SucursalAdmin)


class DirecciónAdmin(admin.ModelAdmin):
    list_display = ('calle_principal', 'calle_secundaria', 'ciudad')
    list_filter = ('calle_principal', 'calle_secundaria', 'ciudad')
    search_fields = ('calle_principal', 'calle_secundaria', 'ciudad')
admin.site.register(Dirección, DirecciónAdmin)

class FarmaciaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    list_filter = ('nombre',)
    search_fields = ('nombre',)
admin.site.register(Farmacia, FarmaciaAdmin)

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('cedula', 'nombre', 'teléfono', 'rol', 'nombre_usuario', )
    list_filter = ('cedula', 'nombre', 'teléfono', 'rol', 'nombre_usuario', )
    search_fields = ('cedula', 'nombre', 'teléfono', 'rol', 'nombre_usuario', )
admin.site.register(Usuario, UsuarioAdmin)
