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

---

## Pagina Principal


Desde esta pagina podemos acceder a los distintos modulos, tambien se pueden visualizar algunas aclaraciones importantes.  

### Imagenes de referencia 

* HomePage en pantallas grandes (width : 920 px )  
![](/static/Home1.png)  
* HomePage en pantallas chicas  
![](/static/Home2.png)  

---

# Modulo Empleados 

Este proyecto contiene un módulo de Empleados que proporciona funcionalidades específicas relacionadas con la gestión de clientes. En este modulo podemos crear, editar, borar, activar y desactivar empleados
por medio de las siguientes urls 


| url                   | Accion                           |
|-----------------------|----------------------------------|
| employee/new/         | Crear un nuevo empleado          |
| employees/list/       | Mostrar una lista de empleado    |
| employee/update/id    | Editar un empleado               |
| employee/delete/id    | Eliminar un empleado             |
| employee/activate/id  | Desactivar empleado              |
| employee/deactivate/id| Desactivar un empleado           |


### Imagenes de Referencia


<img src=".\static\empleados.png">


<img src=".\static\empleados2.png">  

---

## Modulo Coordinadores

En este modulo podemos crear, editar, borrar, activar y desactivar coordinadores 
por medio de las siguientes urls  
  
| url                       | Acción                           |
|---------------------------|----------------------------------|
| coordinator/new           | Crear un nuevo Coordinador       |
| coordinators/list         | Mostrar una lista de Coordinador |
| coordinator/update/id     | Editar un Coordinador            |
| coordinator/delete/id     | Eliminar un Coordinador          |
| coordinator/activate/id   | Activa un Coordinador            |
| coordinator/deactivate/id | Desactiva un Coordinador         |

### Imagenes de referencia  
[](./static/Coordinadores1.png)
[](./static/Coordinadores2.png)
Se utiliza el mismo formulario para crear y para actualizar, las unicas diferencia son:
* Que el formulario para actualizar contendra los datos almacenados del registro que se desea actualizar.
* El boton para confirmar dicha actualizacion posee la leyenda actualizar  

---

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

---

## Modulo Servicios
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

---

## Modulo Reservas
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

---
