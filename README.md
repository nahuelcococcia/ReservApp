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


## Pagina Principal
        URL : ./
Desde esta pagina podemos acceder a los distintos modulos, tambien se pueden visualizar algunas aclaraciones importantes.  

### Imagenes de referencias 

* HomePage en pantallas grandes (width : 920 px )  
![](C:\Pesonal\ReservApp\static\Pagina-Principal.png)  
* HomePage en pantallas chicas  
![](C:\Pesonal\ReservApp\static\Pagina-Principal2.png)  


## Modulo Coordinador

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

### Imagenes de referencias

<img src=".\static\Coordinadores1.png">  
<img src=".\static\Coordinadores2.png">





