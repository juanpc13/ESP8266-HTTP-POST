# ESP8266-HTTP-POST

##Instalación:

### Arduino
-Subir archivo .ino al ESP8266 usando el core correcto usando arduino IDE.

### Linux
Creando el entorno virtual con python : 

$ apt install virtualenv

Instalar el gestor de la base de datos: 

$ apt install sqlite3

Usaremos la base de datos llamada "DB-ESP8266.db" y el archivo python "server.py".
Ambos archivos deben estar en la misma carpeta ya que el archivo .py hace referencia al .db

Creando el entorno virtual:

$ virtualenv venv
$ source venv/bin/activate
$ pip install flask flask-jsonpify flask-sqlalchemy flask-restful
$ pip freeze

Para correr el servicio nuestra terminal debe acceder al entorno virtual (ven).

Iniciar nuestro servicios REST con python en el puerto 5000 con localhost.

$ source venv/bin/activate
$ python server.py

luego podremos hacer peticiones a:

- POST a localhost:5000/temp
- GET a localhost:5000/temp
- GET por ID localhost:5000/temp/1

Las peticiones GET las podemos ver a través del navegador.
Nuestra placa ESP8266 hara POST cada 10 segundos.

Asi es como he llevado acabo este proyecto... Cambiando los headers del archivo .ino podemos adaptarlo a otros Web Services o REST API.
