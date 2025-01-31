from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ( 'cedula','nombre','teléfono','dirección',)
    list_filter = ('cedula','nombre','teléfono','dirección',)
    search_fields = ('cedula','nombre','teléfono','dirección',)

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
    list_display = ('sucursal', 'get_medicamento', 'cantidad_inventario',)
    list_filter = ('sucursal', 'medicamento__nombre_medicamento', 'cantidad_inventario',)
    search_fields = ('sucursal__nombre', 'medicamento__nombre_medicamento', 'cantidad_inventario',)

    def get_medicamento(self, obj):
        return ", ".join([medicamento.nombre_medicamento for medicamento in obj.medicamento.all()])
    get_medicamento.short_description = 'Medicamento'

admin.site.register(Inventario, InventarioAdmin)

class TransferenciaDeMedicamentoAdmin(admin.ModelAdmin):
    list_display = ('medicamento','cantidad_transferencia', 'fecha')
    list_filter = ('medicamento','cantidad_transferencia', 'fecha')
    search_fields = ('cantidad_transferencia', 'fecha')
admin.site.register(TransferenciaDeMedicamento, TransferenciaDeMedicamentoAdmin)


class SucursalAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'dirección', 'teléfono','farmacia')
    list_filter = ('nombre', 'dirección', 'teléfono','farmacia')
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
    model = Usuario
    list_display = ('nombre_usuario', 'nombre', 'cedula', 'rol', 'is_staff', 'is_superuser')
    list_filter = ('rol', 'is_staff', 'is_superuser')
    fieldsets = (
        (None, {'fields': ('nombre_usuario', 'password')}),
        ('Información personal', {'fields': ('nombre', 'cedula', 'teléfono', 'rol')}),
        ('Permisos', {'fields': ('is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Fechas importantes', {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('nombre_usuario', 'password1', 'password2', 'nombre', 'cedula', 'teléfono', 'rol', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
    )
    search_fields = ('nombre_usuario', 'nombre', 'cedula')
    ordering = ('nombre_usuario',)
admin.site.register(Usuario, UsuarioAdmin)


