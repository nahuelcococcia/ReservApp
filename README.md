# ReservApp

## Instalación

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


Desde esta página podemos acceder a los distintos módulos, también se pueden visualizar algunas aclaraciones importantes.  

### Imágenes de referencia 

* HomePage en pantallas grandes (width : 920 px )  
![](/static/imagenes%20de%20referencia/Home1.png)  
* HomePage en pantallas chicas  
![](/static/imagenes%20de%20referencia/Home2.png)  

---

# Modulo Empleados 

Este proyecto contiene un módulo de Empleados que proporciona funcionalidades específicas relacionadas con la gestión de clientes. En este módulo podemos crear, editar, borrar, activar y desactivar empleados
por medio de las siguientes urls 


| url                    | Acción                        |
|------------------------|-------------------------------|
| employee/new/          | Crear un nuevo empleado       |
| employees/list/        | Mostrar una lista de empleado |
| employee/update/id     | Editar un empleado            |
| employee/delete/id     | Eliminar un empleado          |
| employee/activate/id   | Desactivar empleado           |
| employee/deactivate/id | Desactivar un empleado        |


### Imágenes de Referencia


<img src=".\static\imagenes de referencia\empleados.png">


<img src=".\static\imagenes de referencia\empleados2.png">  

---

## Modulo Coordinadores

En este módulo podemos crear, editar, borrar, activar y desactivar coordinadores 
por medio de las siguientes urls  
  
| url                       | Acción                           |
|---------------------------|----------------------------------|
| coordinator/new           | Crear un nuevo Coordinador       |
| coordinators/list         | Mostrar una lista de Coordinador |
| coordinator/update/id     | Editar un Coordinador            |
| coordinator/delete/id     | Eliminar un Coordinador          |
| coordinator/activate/id   | Activa un Coordinador            |
| coordinator/deactivate/id | Desactiva un Coordinador         |

### Imágenes de referencia  
<img src=".\static\imagenes de referencia\Coordinadores1.png">
<img src=".\static\imagenes de referencia\Coordinadores2.png">

Se utiliza el mismo formulario para crear y para actualizar, las únicas diferencia son:
* Que el formulario para actualizar contendrá los datos almacenados del registro que se desea actualizar.
* El botón para confirmar dicha actualización posee la leyenda actualizar  

---

# Módulo de Clientes

Este proyecto contiene un módulo de Clientes que proporciona funcionalidades específicas relacionadas con la gestión de clientes. En este módulo podemos crear, editar, borrar, activar y desactivar clientes
por medio de las siguientes urls  

| url                   | Acción                       |
|-----------------------|------------------------------|
| client/new            | Crear un nuevo cliente       |
| clients/list          | Mostrar una lista de cliente |
| client/update/id      | Editar un cliente            |
| clients/delete/id     | Eliminar un cliente          |
| client/activate/id    | Desactivar cliente           |
| client/deactivate/id  | Desactivar un cliente        |

### Imágenes de referencia  

<img src=".\static\imagenes de referencia\clientes.png">


<img src=".\static\imagenes de referencia\clientes2.png">

---

## Módulo Servicios
En este módulo podemos crear, editar, borrar, activar y desactivar servicios 
por medio de las siguientes urls  
</br>

| url                   | Acción                         |
|-----------------------|--------------------------------|
| service/new           | Crear un nuevo servicio        |
| services/list         | Mostrar una lista de servicios |
| service/update/id     | Editar un servicio             |
| service/delete/id     | Eliminar un servicio           |
| service/activate/id   | Activar un servicio            |
| service/deactivate/id | Desactivar un servicio         |

### Imágenes de referencia
<img src=".\static\imagenes de referencia\service.png">  

 
<img src=".\static\imagenes de referencia\service_form.png">

---

## Módulo Reservas
En este módulo podemos crear, editar y borrar reservas
por medio de las siguientes urls  
</br>

| url                   | Acción                        |
|-----------------------|-------------------------------|
| reserve/new           | Crear una nueva reserva       |
| reserves/list         | Mostrar una lista de reservas |
| reserve/update/id     | Editar una reserva            |
| reserve/delete/id     | Eliminar una reserva          |
 
### Imágenes de referencia

<img src=".\static\imagenes de referencia\reserve.png">  

 
<img src=".\static\imagenes de referencia\reserve_form.png">

---

## API

<table>
    <thead>
    <tr>
        <th>URL</th>
        <th>Descripción</th>
    </tr>
    </thead>
    <tbody>
        <tr>
            <td><p>localhost:8000/api/employees</p></td>
            <td><p>Trae una lista con todos los empleados que están en la base de datos. Devuelve un código 500 en caso de no poder.</p></td>
        </tr>
        <tr>
            <td><p>localhost:8000/api/clients</p></td>
            <td><p>Trae una lista con todos los clientes que están en la base de datos. Devuelve un código 500 en caso de no poder</p></td>
        </tr>
        <tr>
            <td><p>localhost:8000/api/coordinators</p></td>
            <td><p>Trae una lista con todos los coordinadores que están en la base de datos. Devuelve un código 500 en caso de no poder</p></td>
        </tr>
        <tr>
            <td><p>localhost:8000/api/services</p></td>
            <td><p>Trae una lista con todos los servicios que están en la base de datos. Devuelve un código 500 en caso de no poder</p></td>
        </tr>
        <tr>
            <td><p>localhost:8000/api/services/id</p></td>
            <td><p>Pasando el ID por url, devuelve un determinado servicio. Devuelve un código 404 en caso de encontrar el servicio.</p></td>
        </tr>
    </tbody>
</table>

---

## Admin

En este apartado podremos hacer uso de las funcionalidades de CRUD los distintos modulos pero también del CRUD de usuarios y grupos.  
Asignamos un enlace a este apartado en la barra de navegación para facilitar su acceso.  
Además de poder acceder a la página se debe crear un usuario desde la terminal posicionándose sobre la carpeta donde se encuentra el proyecto, luego verificar que exista el archivo ___manage.py___ y utilizar el siguiente comando:  

    python manage.py createsuperuser  

Lo siguiente será proporcionar un nombre de usuario y una contraseña.  
Luego de realizar este proceso tendrá acceso a las funcionalidades del tipo Admin.  
Desde esta sección se visualizan los modelos correspondientes a Employee, Coordinator, Client, Service y ReserveService
A continuación se realizará un resumen de los modelos y los atributos:  

#### Modelos y atributos  
* **_Client_**
  * id
  * name
  * lastname
  * is_active
  
* **_Coordinator_**
  * name
  * lastname
  * dni_number
  * is_active
  
* **_Employee_**
  * name
  * lastname
  * file_number
  * is_active
  
* **_ReserveService_**
  * creation_date
  * reservation_date
  * client
  * Employee
  * Service
  * price
  
* **_Services_**
  * name
  * description
  * price
  * is_active

### Imágenes de referencia
* Consola pidiendo nombre y contraseña.  
![](/static/imagenes%20de%20referencia/Admin1.png)
* Pantalla del Admin mostrando los modelos  
![](/static/imagenes%20de%20referencia/Admin2.png)  
* Posibles acciones desde el Admin  
![](/static/imagenes%20de%20referencia/Admin3.png) 