# Realtime con websockets y flask

_Recibe ordenes mediante una api y muestra cambios realizados mediante websockets_


### Requisitos
```
Python 3
Pip
Cmake
```


### Instalación
* Clona o descarga el proyecto
* Ingresa a la carpeta raiz del proyecto del proyecto

_En consola_

```
# pip install virtualenv

# virtualenv my-env -p python3
# source my-env/bin/activate
# pip install -r requirements.txt
# make start-app o python3 run.py 
```

### Pruebas 
```
# pytest
```

### Ejemplo de uso
Inicia la aplicación 
Para ver las ordenes que van llegando esde el navegador ingresa a la url (http://localhost:5000/admin/orders/)

Ahora para envíar ordenes realiza una petición POST al siguiente endpoint (localhost:5000/api/orders/) y en el body del requst envía los siguiente esquema json
```
{
    "orden": "1 burrito",
    "direccion_cliente": "Lago iseo 268",
    "telefono_cliente": "1234567",
    "nombre_cliente": "Peter Equis"
}
```


En la interfaz web apareceran cada solicitud recibida
