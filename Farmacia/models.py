from typing import Any

from django.contrib.auth.models import AbstractUser
from django.db import models
from enum import Enum
# Create your models here.
class Rol(Enum):
    CLIENTE = 'Cliente'
    EMPLEADO = 'Empleado'
    ADMINISTRATIVO = 'Administrativo'

class TipoDePago(Enum):
    EFECTIVO = 'Efectivo'
    TARJETA = 'Tarjeta'
    TRANSFERENCIA = 'Transferencia'

class Presentación(Enum):
    LIQUIDO = 'Líquido'
    SOLIDO = 'Sólido'
    SEMISOLIDO = 'Semisólido'

class Persona(models.Model):
    cedula = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=50)
    teléfono = models.CharField(max_length=10)

    class Meta:
        abstract = True

    def __str__(self):
        return self.nombre + ' ' + self.cedula + ' ' + self.teléfono

class Cliente(Persona):

    dirección = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Usuario(Persona):
    rol = models.CharField(max_length=50,
        choices=[(tag.name, tag.value) for tag in Rol])
    nombre_usuario = models.CharField(max_length=50)
    contraseña = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.rol} {self.nombre_usuario} {self.contraseña}'


class Dirección(models.Model):
    calle_principal = models.CharField(max_length=50)
    calle_secundaria = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.calle_principal} {self.calle_secundaria} {self.ciudad}'


class Farmacia(models.Model):
    nombre = models.CharField(max_length=50)


    def __str__(self):
        return self.nombre

class Sucursal(models.Model):
    nombre = models.CharField(max_length=50)
    dirección = models.ForeignKey(Dirección, on_delete=models.CASCADE)
    teléfono = models.CharField(max_length=10)
    farmacia = models.ForeignKey('Farmacia', on_delete=models.CASCADE, related_name='sucursales')

    def __str__(self):
        return f'{self.nombre} {self.dirección} {self.teléfono}'


class Empleado(Persona):
    identificación = models.CharField(max_length=10)
    sueldo = models.FloatField()
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE, related_name='empleados')

    class Meta:
        abstract = True

    def __str__(self):
        return f'{self.identificación} {self.sueldo} {self.sucursal}'

class Administrativo(Empleado):
    cargo = models.CharField(max_length=50)
    horario = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.cargo} {self.horario}'

class Venta(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE)
    tipo_pago = models.CharField(max_length=50,
        choices=[(tag.name, tag.value) for tag in TipoDePago])
    fecha = models.DateField()
    total = models.FloatField()

    def __str__(self):
        return f'{self.cliente} {self.sucursal} {self.tipo_pago} {self.fecha} {self.total}'

class Medicamento(models.Model):
    nombre_medicamento = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)
    presentación = models.CharField(
        max_length=50,
        choices=[(tag.name, tag.value) for tag in Presentación]  # Usamos los valores del Enum
    )
    def __str__(self):
        return f'{self.nombre_medicamento} {self.descripcion} {self.presentación}'

class Inventario(models.Model):
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE, related_name='inventarios')
    medicamento = models.ManyToManyField(Medicamento, related_name='inventarios')
    cantidad_inventario = models.IntegerField()

    def __str__(self):
        return f'{self.sucursal} {self.medicamento} {self.cantidad_inventario}'

class TransferenciaDeMedicamentos(models.Model):
    sucursal_origen = models.ForeignKey(Sucursal, on_delete=models.CASCADE, related_name='transferencias_origen')
    sucursal_destino = models.ForeignKey(Sucursal, on_delete=models.CASCADE, related_name='transferencias_destino')
    medicamento = models.ForeignKey(Medicamento, on_delete=models.CASCADE, related_name='transferencias')
    cantidad_transferencia = models.IntegerField()
    fecha = models.DateField()

    def __str__(self):
        return (f'{self.sucursal_origen} {self.sucursal_destino} '
                f'{self.medicamento} {self.cantidad_transferencia} {self.fecha}')


class DetalleVenta(models.Model):
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE, related_name='detalles_venta')
    medicamento = models.ForeignKey(Medicamento, on_delete=models.CASCADE, related_name='detalles_venta')
    cantidad_medicamento = models.IntegerField()
    precio = models.FloatField()

    def __str__(self):
        return f'{self.venta} {self.medicamento} {self.cantidad_medicamento} {self.precio}'