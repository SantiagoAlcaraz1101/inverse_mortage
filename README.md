# Proyecto de Aula: Hipoteca Inversa

## Descripción

Este proyecto de aula tiene como objetivo desarrollar un sistema que permita simular y analizar el funcionamiento de la hipoteca inversa. Se busca proporcionar herramientas para calcular y visualizar escenarios en los que una persona pueda convertir su vivienda en una fuente de ingresos sin perder su propiedad mientras viva.

## Equipo de Trabajo

- **Docente**: William David Velásquez

- **Integrantes del equipo**: Emanuel García Rios y Juan José Becerra

- **Integrantes GUI**: Miguel Angel Salas, Juan Esteban Marin


## Objetivos

- Implementar un sistema que simule la hipoteca inversa.

- Permitir la personalización de parámetros como el valor de la vivienda, la edad del solicitante, tasas de interés, entre otros.

- Generar reportes y gráficos que faciliten la comprensión del resultado de la hipoteca inversa.

- Ofrecer una interfaz amigable para el usuario.

## Como ejecutarlo:
1. Instalar las dependencias necesarias:
```bash
pip install numpy
pip install matplotlib
pip install kivy
pip install psycopg2
```

2. Configurar las credenciales de la base de datos en la carpeta config (ver sección Configuración de Credenciales).

3. Ejecutar el proyecto desde la carpeta raíz:
- Por consola:
```
python3 src/view/console/console.py
```

- Por interfaz gráfica:

```
python3 src/view/gui/main.py
```

> **Nota**: Es importante ejecutar los comandos desde la carpeta raíz para que las rutas relativas funcionen correctamente.

## Configuración de Credenciales
Para que el proyecto funcione correctamente, debes crear un archivo llamado secret_config.py dentro de la carpeta config. Este archivo debe contener las credenciales de la base de datos PostgreSQL en el siguiente formato:

```
PGHOST = "tu_host"
PGDATABASE = "tu_base_de_datos"
PGUSER = "tu_usuario"
PGPASSWORD = "tu_contraseña"
```
> **Nota**: Recuerda agregar quitar tus keys o agregar al gitignore.

### Ingreso de Datos:

- Valor de la vivienda.

- Edad del solicitante.

- Tasas de interés y condiciones del préstamo.


### Cálculo de Pago Mensual:

- Determinar el monto mensual que recibiría el solicitante según las condiciones ingresadas.


### Generación de Reportes:

- Gráficos y tablas con la evolución del préstamo.

- Permitir la descarga de los resultados en formatos CSV o PDF.


## Estructura del Proyecto

La estructura de carpetas y archivos del proyecto es la siguiente:

```
/inverse_mortage/
├── README.md
├── config/
│   └── secret_config.py
├── src/
│   ├── controller/
│   │   ├── personas_controller.py
│   │   └── propiedades_controller.py
│   ├── model/
│   │   ├── inverse_mortage.py
│   │   ├──  exceptions.py
│   │   └── property_value.py
│   ├── sql/
│   │   ├── create_table_person.sql
│   │   ├── create_table_property.sql
│   │   ├── delete_person.sql
│   │   ├── delete_property.sql
│   │   ├── insert_persona.sql
│   │   ├── insert_property.sql
│   │   ├── select_person.sql
│   │   ├── select_property.sql
│   │   ├── update_person.sql
│   │   ├── update_propery.sql
│   └── view/
│       ├── console/
│       │   └── console.py
│       └── gui/
│           └── main.py
├── tests/
│   ├── test.py
├
├── .gitignore

```

### Instrucciones para Pruebas Unitarias

1. Configura un framework de pruebas con `unittest`
2. Crea archivos de prueba separados, como `test_<nombre_del_módulo>.py`.
3. Ejecuta las pruebas con herramientas `python -m unittest`.


## Casos de Estudio

Los casos específicos para el análisis del proyecto se encuentran en el siguiente enlace de Google Sheets:

https://docs.google.com/spreadsheets/d/13gb_k_L8XEZlQfSJO_waRds3wgISHP0f5UH5qSc5wlM/edit?usp=sharing

## Artículo sobre Hipoteca Inversa - Universidad de Medellín
https://repository.udem.edu.co/bitstream/handle/11407/6356/T_MF_436.pdf?sequence=2&isAllowed=y


## Tecnologías Utilizadas

- Lenguaje de Programación: Python X

- Frameworks: Django / Flask (según preferencia) X

- Base de Datos: PostgreSql

- Generación de interfaz gráfica: kivy
