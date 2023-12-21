# Nombre de mi blog

_Aplicacion web diseñada por el grupo ___  de la comision 7 del informatorio, segunda cohorte de 2023.
Consiste en un blog para la divulgacion de informacion referida a VIDEOJUEGOS/LIBROS_

## Comenzando 🚀

_Para obtener una copia del proyecto funcionando en tu PC de manera local para propósitos de desarrollo y pruebas, seguí las instrucciones_


### Pre-requisitos 📋

_Antes de iniciar, es recomendable generar un entorno virtual de trabajo donde instalaremos las dependencias necesarias para que el proyecto funcione. Para ello, abrimos el CMD y nos dirigimos a la carpeta donde queremos guardar el entorno virtual y ejecutamos el siguiente comando:_


```
python3 -m venv nombre_del_entorno

```
_Una vez creado es necesario activarlo para ello ejecutamos la siguiente linea (en Windows):_


```
nombre_del_entorno\Scripts\activate.bat

```

_Ya contamos con un entorno virtual activado en el cual podemos instalar todas las dependencias para correr nuestro proyecto._


_Luego, con el entorno activado, no dirigimos a la carpeta donde se encuentra el archivo requirements.txt y ejecuta el siguiente comando en la consola._

```
pip install -r requirements.txt

```
_Este comando instalará en nuestro entorno, todo lo necesario para que el proyecto funcione funciona correctamente._

### SETTINGS 🔧

Luego tenes que crear un archivo de configuraciones en la carpeta fundacion_pueblo/settings/ y llamala "local.py", donde debes indicar las credenciales de tu base de datos como se muestra a continuacion.

```
from .base import *


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', 
        'NAME': 'databaseName',
        'USER': 'databaseUser',
        'PASSWORD': 'databasePassword',
        'HOST': 'localhost',
        'PORT': 'portNumber',
    }
}

```


## Construido con 🛠️

_Las herramientas utilizadas para el desarrollo fueron:_

* [Django](https://www.djangoproject.com/) Framework web
* [Python](https://www.python.org/) Del lado del servidor (backend)
* [Bootstrap](https://getbootstrap.com/) Framework web para el desarrollo frontend (HTML, CSS, JavaScript)
* [MySql](https://www.mysql.com/) - Sistema de gestión de bases de datos.


## Autores ✒️

_Este proyecto fue desarrollado gracias a la colaboración de:_

* **Tomas Martinez** - Docente - Desarrollo WEB y Bases de Datos.

* **Cosme Fulanito** 
* **Mengano Gomez** 



También puedes mirar la lista de todos los [contribuyentes](https://github.com/tomimartinez28/blog-comision-7/graphs/contributors) quíenes han participado en este proyecto. 




---
