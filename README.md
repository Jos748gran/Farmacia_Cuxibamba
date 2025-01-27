# Proyecto Farmacia

Este proyecto es una aplicación web para la gestión de una farmacia, desarrollada con Django. La aplicación permite gestionar clientes, usuarios, ventas, inventarios, transferencias de medicamentos, entre otros.

## Características

- **Gestión de clientes**: Permite registrar, actualizar y eliminar información de los clientes.
- **Gestión de usuarios**: Administra los usuarios del sistema con diferentes roles.
- **Gestión de ventas**: Registra las ventas realizadas en la farmacia.
- **Gestión de inventarios**: Controla el stock de medicamentos en las diferentes sucursales.
- **Transferencias de medicamentos**: Facilita la transferencia de medicamentos entre sucursales.
- **Administración de sucursales y direcciones**: Gestiona la información de las sucursales y sus ubicaciones.

## Tecnologías Utilizadas

- **Lenguaje de programación**: Python
- **Framework web**: Django 5.1.5
- **Base de datos**: MySQL
- **Conectores de base de datos**: `mysql-connector-python`, `mysqlclient`
- **Otros paquetes**: `asgiref`, `sqlparse`, `tzdata`, `views`

## Instalación

Sigue estos pasos para configurar y ejecutar el proyecto en tu entorno local:

1. Clona el repositorio:
    ```bash
    git clone https://github.com/tu_usuario/tu_repositorio.git
    ```
2. Navega al directorio del proyecto:
    ```bash
    cd tu_repositorio
    ```
3. Crea un entorno virtual:
    ```bash
    python -m venv env
    ```
4. Activa el entorno virtual:
    - En Windows:
        ```bash
        .\env\Scripts\activate
        ```
    - En macOS/Linux:
        ```bash
        source env/bin/activate
        ```
5. Instala las dependencias:
    ```bash
    pip install -r requirements.txt
    ```
6. Realiza las migraciones:
    ```bash
    python manage.py migrate
    ```
7. Ejecuta el servidor de desarrollo:
    ```bash
    python manage.py runserver
    ```

## Uso

Accede a la aplicación en tu navegador web en `http://127.0.0.1:8000/`.

## Modelos

### Cliente
- `cedula`: Identificación del cliente.
- `nombre`: Nombre del cliente.
- `teléfono`: Número de teléfono del cliente.
- `dirección`: Dirección del cliente.

### Usuario
- `cedula`: Identificación del usuario.
- `nombre`: Nombre del usuario.
- `teléfono`: Número de teléfono del usuario.
- `rol`: Rol del usuario en el sistema.
- `nombre_usuario`: Nombre de usuario para el inicio de sesión.
- `contraseña`: Contraseña del usuario.

### Venta
- `cliente`: Cliente que realiza la compra.
- `sucursal`: Sucursal donde se realiza la venta.
- `tipo_pago`: Tipo de pago utilizado.
- `fecha`: Fecha de la venta.
- `total`: Total de la venta.

### DetalleVenta
- `venta`: Venta a la que pertenece el detalle.
- `medicamento`: Medicamento vendido.
- `cantidad_medicamento`: Cantidad de medicamento vendido.
- `precio`: Precio del medicamento.

### Medicamento
- `nombre_medicamento`: Nombre del medicamento.
- `descripcion`: Descripción del medicamento.
- `presentación`: Presentación del medicamento (tabletas, jarabe, etc.).

### Inventario
- `sucursal`: Sucursal donde se encuentra el inventario.
- `medicamento`: Medicamento en inventario.
- `cantidad_inventario`: Cantidad de medicamento en inventario.

### TransferenciaDeMedicamentos
- `sucursal_origen`: Sucursal de origen de la transferencia.
- `sucursal_destino`: Sucursal de destino de la transferencia.
- `medicamento`: Medicamento transferido.
- `cantidad_transferencia`: Cantidad de medicamento transferido.
- `fecha`: Fecha de la transferencia.

### Sucursal
- `nombre`: Nombre de la sucursal.
- `dirección`: Dirección de la sucursal.
- `teléfono`: Teléfono de la sucursal.
- `farmacia`: Farmacia a la que pertenece la sucursal.

### Dirección
- `calle_principal`: Calle principal de la dirección.
- `calle_secundaria`: Calle secundaria de la dirección.
- `ciudad`: Ciudad de la dirección.

### Farmacia
- `nombre`: Nombre de la farmacia.

## Diagrama UML

![Farmacia](https://github.com/user-attachments/assets/069d6e81-9506-4337-a4c6-196a6d74ad21)



## Autor

Carlos Josué Granda Cango
