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

## API

<table>
    <thead>
    <tr>
        <th>URL</th>
        <th>Descripcion</th>
    </tr>
    </thead>
    <tbody>
        <tr>
            <td><p>localhost:8000/api/employees</p></td>
            <td><p>Trae una lista con todos los empleados que estan en la base de datos. Devuelve devuelve un codigo 500 en caso de no poder.</p></td>
        </tr>
        <tr>
            <td><p>localhost:8000/api/clients</p></td>
            <td><p>Trae una lista con todos los clientes que estan en la base de datos. Devuelve devuelve un codigo 500 en caso de no poder</p></td>
        </tr>
        <tr>
            <td><p>localhost:8000/api/coordinators</p></td>
            <td><p>Trae una lista con todos los coordinadores que estan en la base de datos. Devuelve devuelve un codigo 500 en caso de no poder</p></td>
        </tr>
        <tr>
            <td><p>localhost:8000/api/services</p></td>
            <td><p>Trae una lista con todos los servicios que estan en la base de datos. Devuelve devuelve un codigo 500 en caso de no poder</p></td>
        </tr>
        <tr>
            <td><p>localhost:8000/api/services/id</p></td>
            <td><p>Pasando el id por url, devuelve un determinado servicio. Devulve un codigo 404 en caso de encontrar el servicio.</p></td>
        </tr>
    </tbody>
</table>