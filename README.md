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

## Servicios
En este modulo podemos crear, editar, borar, activar y desactivar servicios 
por medio de las siguientes urls  
</br>

| url                   | Accion                           |
|-----------------------|----------------------------------|
| service/new           | Crear un nuevo servicio          |
| services/list         | Mostrar una lista de servicios   |
 | service/update/id     | Editar un servicio               |
| service/delete/id     | Eliminar un servicio             |
| service/activate/id   | Activar un servicio              |
| service/deactivate/id | Desactivar un servicio           |

### Imagenes de referencia
<img src=".\static\service.png">  

 
<img src=".\static\service_form.png">


## Reservas
En este modulo podemos crear, editar y  borar reservas
por medio de las siguientes urls  
</br>

| url                   | Accion                        |
|-----------------------|-------------------------------|
| reserve/new           | Crear una nueva reserva       |
| reserves/list         | Mostrar una lista de reservas |
 | reserve/update/id     | Editar una reserva            |
| reserve/delete/id     | Eliminar una reserva          |
 
### Imagenes de referencia

<img src=".\static\reserve.png">  

 
<img src=".\static\reserve_form.png">