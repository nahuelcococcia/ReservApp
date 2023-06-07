# Pagina de reservas ReservApp

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
![](/static/Admin1.png)
* Pantalla del Admin mostrando los modelos  
![](/static/Admin2.png)  
* Posibles acciones desde el Admin  
![](/static/Admin3.png) 





