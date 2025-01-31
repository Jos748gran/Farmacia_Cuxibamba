# Farmacia Cuxibamba

Este proyecto es una aplicación web para la gestión de una farmacia, desarrollada con Django. Permite gestionar clientes, empleados, medicamentos, ventas, inventarios, transferencias de medicamentos y más.

## Características

- Gestión de usuarios con roles (Cliente, Empleado, Administrativo)
- CRUD de clientes, empleados, medicamentos, ventas, inventarios, transferencias de medicamentos, direcciones, farmacias, sucursales y detalles de venta
- Autenticación y autorización de usuarios
- Sistema de gestión con interfaz amigable

## Requisitos

- Python 3.8+
- Django 5.1.5
- SQLite (base de datos por defecto)

## Instalación

1. Clona el repositorio:
    ```bash
    git clone https://github.com/Carlosjosu/Farmacia_Cuxibamba.git
    cd Farmacia_Cuxibamba
    ```

2. Crea y activa un entorno virtual:
    ```bash
    python -m venv env
    source env/bin/activate  # En Windows usa `env\Scripts\activate`
    ```

3. Instala las dependencias:
    ```bash
    pip install -r requirements.txt
    ```

4. Realiza las migraciones de la base de datos:
    ```bash
    python manage.py migrate
    ```

5. Crea un superusuario:
    ```bash
    python manage.py createsuperuser
    ```

6. Inicia el servidor de desarrollo:
    ```bash
    python manage.py runserver
    ```

7. Accede a la aplicación en tu navegador:
    ```
    http://127.0.0.1:8000
    ```

## Uso

### Gestión de Usuarios

- Registro de nuevos usuarios
- Inicio de sesión
- Cambio de contraseña
- Restablecimiento de contraseña

### Gestión de Clientes

- Crear, leer, actualizar y eliminar clientes

### Gestión de Empleados

- Crear, leer, actualizar y eliminar empleados

### Gestión de Medicamentos

- Crear, leer, actualizar y eliminar medicamentos

### Gestión de Ventas

- Crear, leer, actualizar y eliminar ventas

### Gestión de Inventarios

- Crear, leer, actualizar y eliminar inventarios

### Gestión de Transferencias de Medicamentos

- Crear, leer, actualizar y eliminar transferencias de medicamentos

### Gestión de Direcciones

- Crear, leer, actualizar y eliminar direcciones

### Gestión de Farmacias

- Crear, leer, actualizar y eliminar farmacias

### Gestión de Sucursales

- Crear, leer, actualizar y eliminar sucursales

### Gestión de Detalles de Venta

- Crear, leer, actualizar y eliminar detalles de venta

## UML

![Farmacia](https://github.com/user-attachments/assets/a7b75417-60e7-4c5b-a382-f8eecce341c1)

## Capturas de Pantalla

### Página Principal

![image](https://github.com/user-attachments/assets/177cecfb-1d15-41a7-80f1-14d0e1c227c8)

### Inicio de Sesion

![image](https://github.com/user-attachments/assets/0d6f80a7-0182-4dd9-b2be-8be0ed3a917b)

### Registrar Usuario

![image](https://github.com/user-attachments/assets/e04b1183-1223-4ba1-b994-1b55018b4a75)

### Interfaz

![image](https://github.com/user-attachments/assets/25bf719e-7bc8-4afa-aa76-4c6bb0252632)

### Capturas Adicionales
![image](https://github.com/user-attachments/assets/2a514b77-fb4a-466a-a127-95a71b011a31)
![image](https://github.com/user-attachments/assets/362c9bf0-548c-402d-afd1-6bbaccac6a9e)
![image](https://github.com/user-attachments/assets/94fae14e-6e63-4366-a513-7c2088594406)


## Autor

Carlos Josué Granda Cango
