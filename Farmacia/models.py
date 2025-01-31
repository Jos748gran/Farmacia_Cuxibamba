from typing import Any

from django.db import transaction
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models
from enum import Enum
from django.contrib.auth.models import Group, Permission

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

    def realizar_compra_de_venta_en_medicamentos(self):
        pass

    def __str__(self):
        return self.nombre


class UsuarioManager(BaseUserManager):
    def create_user(self, nombre_usuario, password=None, **extra_fields):
        if not nombre_usuario:
            raise ValueError('El nombre de usuario debe ser proporcionado')
        user = self.model(nombre_usuario=nombre_usuario, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        if user.rol == 'EMPLEADO':
            group = Group.objects.get(name='Empleados')
        elif user.rol == 'CLIENTE':
            group = Group.objects.get(name='Clientes')
        elif user.rol == 'ADMINISTRATIVO':
            group = Group.objects.get(name='Administradores')
        else:
            group = None

        if group:
            user.groups.add(group)

        return user

    def create_superuser(self, nombre_usuario, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(nombre_usuario, password, **extra_fields)

class Usuario(Persona, AbstractBaseUser, PermissionsMixin):
    rol = models.CharField(max_length=50, choices=[(tag.name, tag.value) for tag in Rol])
    nombre_usuario = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=256)
    last_login = models.DateTimeField(blank=True, null=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    groups = models.ManyToManyField(Group, related_name='usuario_set', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='usuario_set', blank=True)

    USERNAME_FIELD = 'nombre_usuario'
    REQUIRED_FIELDS = ['cedula', 'nombre', 'teléfono', 'rol']

    objects = UsuarioManager()

    def __str__(self):
        return self.nombre_usuario


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
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE,related_name='ventas')
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE)
    tipo_pago = models.CharField(max_length=50,
        choices=[(tag.name, tag.value) for tag in TipoDePago])
    fecha = models.DateField()
    total = models.FloatField()
    def calcular_total(self):
        pass

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
    medicamento  = models.ManyToManyField(Medicamento, related_name='inventarios')
    cantidad_inventario = models.IntegerField()

    def __str__(self):
        medicamento = ", ".join([medicamento.nombre_medicamento for medicamento in self.medicamento.all()])
        return f'{self.sucursal} {medicamento} {self.cantidad_inventario}'

class TransferenciaDeMedicamento(models.Model):
    sucursal_origen = models.ForeignKey(Sucursal, on_delete=models.CASCADE, related_name='transferencias_origen')
    sucursal_destino = models.ForeignKey(Sucursal, on_delete=models.CASCADE, related_name='transferencias_destino')
    medicamento = models.ForeignKey(Medicamento, on_delete=models.CASCADE, related_name='transferencias')
    cantidad_transferencia = models.IntegerField()
    fecha = models.DateField()

    def __str__(self):
        return (f'{self.sucursal_origen} {self.sucursal_destino} '
                f'{self.medicamento} {self.cantidad_transferencia} {self.fecha}')

    def realizar_transferencia(self):
        pass


class DetalleVenta(models.Model):
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE, related_name='detalles_venta')
    medicamento = models.ForeignKey(Medicamento, on_delete=models.CASCADE, related_name='detalles_venta')
    cantidad_medicamento = models.IntegerField()
    precio = models.FloatField()

    def __str__(self):
        return f'{self.venta} {self.medicamento} {self.cantidad_medicamento} {self.precio}'

