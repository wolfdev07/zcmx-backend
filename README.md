# Zip Code MX

Este proyecto permite cargar y gestionar datos de códigos postales, estados, municipios y asentamientos en México utilizando una base de datos PostgreSQL.

## Requisitos

- Python 3.8+
- PostgreSQL
- Paquetes de Python listados en `requirements.txt`

## Instalación

1. Clona el repositorio:

    ```bash
    git clone https://github.com/tu-usuario/zip-code-mx.git
    cd zip-code-mx
    ```

2. Crea un entorno virtual y activa el entorno:

    ```bash
    python -m venv env
    source env/bin/activate  # En Windows usa `env\Scripts\activate`
    ```

3. Instala las dependencias:

    ```bash
    pip install -r requirements.txt
    ```

## Configuración de la Base de Datos

1. Asegúrate de tener PostgreSQL instalado y ejecutándose.

2. Crea una base de datos para el proyecto:

    ```sql
    CREATE DATABASE zip_code_mx;
    ```

3. Conéctate a la base de datos y habilita la extensión `pg_trgm`:

    ```sql
    \c zip_code_mx
    CREATE EXTENSION IF NOT EXISTS pg_trgm;
    ```

4. Crea las tablas necesarias:

    ```sql
    CREATE TABLE zip_codes_mx_state (
        entity_number INTEGER PRIMARY KEY,
        name VARCHAR(255),
        search_vector TSVECTOR
    );

    CREATE TABLE zip_codes_mx_municipality (
        id SERIAL PRIMARY KEY,
        state_id INTEGER REFERENCES zip_codes_mx_state(entity_number),
        name VARCHAR(255),
        search_vector TSVECTOR
    );

    CREATE TABLE zip_codes_mx_city (
        id SERIAL PRIMARY KEY,
        municipality_id INTEGER REFERENCES zip_codes_mx_municipality(id),
        name VARCHAR(255),
        search_vector TSVECTOR
    );

    CREATE TABLE zip_codes_mx_postalcode (
        id SERIAL PRIMARY KEY,
        city_id INTEGER REFERENCES zip_codes_mx_city(id),
        code VARCHAR(5)
    );

    CREATE TABLE zip_codes_mx_settlement (
        id SERIAL PRIMARY KEY,
        postal_code_id INTEGER REFERENCES zip_codes_mx_postalcode(id),
        name VARCHAR(255),
        settlement_type VARCHAR(255),
        search_vector TSVECTOR
    );
    ```

## Uso

1. Asegúrate de que tu base de datos esté configurada correctamente y que el archivo `utils.py` contenga la función `get_db_connection()` que devuelve una conexión a tu base de datos.

2. Coloca tu archivo Excel en la ubicación adecuada y actualiza la URL del archivo en el script principal.

3. Ejecuta el script para cargar los datos:

    ```python
    import pandas as pd
    import unicodedata
    from utils import get_db_connection

    # Tu código aquí...
    ```

## Endpoints

El proyecto incluye un endpoint Flask para actualizar la base de datos:

1. Asegúrate de tener Flask instalado y configurado en tu entorno.

2. Ejecuta la aplicación Flask:

    ```bash
    export FLASK_APP=main.py
    flask run
    ```

3. Accede al endpoint para actualizar la base de datos:

    ```
    GET /update_database
    ```

## Funciones

### vector_build

Convierte una palabra en un vector de búsqueda.

```python
def vector_build(word):
    # Implementación...
