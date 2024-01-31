# Desafio Tecnico IngeniaSoft
### Requisitos
- Tener Docker
- Tener Python 3.9+
### Instrucciones
- (Opcional) Correr `python -m venv venv`, para generar el entorno virtual.
- (Opcional) Correr `venv\Scripts\Activate`, para ir a un entorno virtual. 
- Correr `docker-compose up -d`
- Ir a `localhost:8000/docs`
- Probar las CRUDS!
- Para detener el contenedor correr `docker-compose down`
- Para salir del enotrno virtual, correr `deactivate`

### Consideraciones
- Las variables de entornos estan dockerizadas. `DATABASE_URL` se encuentra en el archivo `docker-compose.yaml`
- La diferencia entre rango mínimo y máximo se le suma uno, ya que por ejemplo entre 30 y 0 hay 31 valores.
- Para el CRUD de Actualizar chequeras solo se puede cambiar el nombre de la esta misma, para evitar conflictos al modificar los rangos.
- Para el CRUD de Borrar una Chequera, se consideró que se debían eliminar los cheques de la chequera.
- En el CRUD de Actualizar un Cheque, es posible transferir el cheque a otra chequera.
