# Pagina de reservas ReservApp

## Instalacion

Abrir una consola

Clonar el repositorio

> git clone https://github.com/nahuelcococcia/ReservApp.git

Instalar los requerimientos

> pip install -r requirements.txt

Realizar las migraciones correspondientes

> python manage.py migrate 

Levantar el entorno virtual

> python -m venv (nombre de carpeta. Por defecto 'env' )\
> por ejemplo : python -m venv env

Activar el entorno virtual

> env\Scripts\activate

Correr el servidor

> python manage.py runserver

---------------------------------------------------------------------------------------------------------------------------------

# Módulo de Clientes

Este proyecto contiene un módulo de Clientes que proporciona funcionalidades específicas relacionadas con la gestión de clientes. En este modulo podemos crear, editar, borar, activar y desactivar clientes
por medio de las siguientes urls  

| url                   | Accion                           |
|-----------------------|----------------------------------|
| client/new            | Crear un nuevo cliente           |
| clients/list          | Mostrar una lista de cliente     |
| client/update/id      | Editar un cliente                |
| clients/delete/id     | Eliminar un cliente              |
| client/activate/id    | Desactivar cliente               |
| client/deactivate/id  | Desactivar un cliente            |

### Imagenes de referencia  

<img src=".\static\clientes.png">


<img src=".\static\clientes2.png">

