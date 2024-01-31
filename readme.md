# Desafio Tecnico IngeniaSoft
### Requisitos
- Tener Docker
- Tener Python 3.9+
### Instrucciones
- Correr `python -m venv venv`, para generar el entorno virtual.
- Correr `venv\Scripts\Activate`, para ir a un entorno virtual.
- Correr `docker-compose up -d`
- Ir a `localhost:8000/docs`
- Probar las CRUDS!
- Para detener el contenedor correr `docker-compose down`
- Para salir del enotrno virtual, correr `deactivate`

### Consideraciones
- Las variables de entornos estan dockerizadas. `DATABASE_URL` se encuentra en el archivo `docker-compose.yaml`
- La diferencia entre rango minimo y maximo se le resta uno, ya que por ejemplo entre 30 y 0 hay 31 valores.
- Para el CRUD de Actualizar chequeras solo se puede cambiar el nombre de esta, para evitar conflictos al modificar los rangos.
- Para el CRUD de Borrar una Chequera, se considero que se debian eliminar los cheques que esta posee.
- En el CRUD de Actualizar un Cheque, es posible transferir el cheque a otra chequera.