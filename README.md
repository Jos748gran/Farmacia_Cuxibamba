# Farmacia Cuxibamba

Este proyecto es una aplicación web para la gestión de una farmacia, desarrollada con Django. Permite gestionar clientes, empleados, medicamentos, ventas, inventarios, transferencias de medicamentos y más.

## Características

- Gestión de usuarios con roles (Cliente, Empleado, Administrativo)
- CRUD de clientes, empleados, medicamentos, ventas, inventarios y transferencias de medicamentos
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

3. Realiza las migraciones de la base de datos:
    ```bash
    python manage.py migrate
    ```

4. Crea un superusuario:
    ```bash
    python manage.py createsuperuser
    ```

5. Inicia el servidor de desarrollo:
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

## UML

![Farmacia](https://github.com/user-attachments/assets/950b5102-131e-47c8-bd6d-2ade181ee04e)

## Capturas de Pantalla

### Página Principal

![image](https://github.com/user-attachments/assets/3c06e05c-922b-473b-9591-7567ce101b61)

### Inicio de Sesion

![image](https://github.com/user-attachments/assets/793136ff-8e83-4721-95b4-fc2c722e9bbc)

### Registrar Usuario
![image](https://github.com/user-attachments/assets/ee9e6db2-5490-47fb-8283-dad9d10303cb)

### Interfaz
![image](https://github.com/user-attachments/assets/2e77ae89-3996-49b6-933d-76407d8f1351)


## Autor

Carlos Josué Granda Cango
