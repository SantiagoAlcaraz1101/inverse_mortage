# Proyecto de Aula: Hipoteca Inversa

## Descripción

Este proyecto de aula tiene como objetivo desarrollar un sistema que permita simular y analizar el funcionamiento de la hipoteca inversa. Se busca proporcionar herramientas para calcular y visualizar escenarios en los que una persona pueda convertir su vivienda en una fuente de ingresos sin perder su propiedad mientras viva.

## Objetivos

- Implementar un sistema que simule la hipoteca inversa.

- Permitir la personalización de parámetros como el valor de la vivienda, la edad del solicitante, tasas de interés, entre otros.

- Generar reportes y gráficos que faciliten la comprensión del resultado de la hipoteca inversa.

- Ofrecer una interfaz amigable para el usuario.

## Funcionalidades

### Como ejecutarlo:

pip install numpy

py src/view/gui/console.py

 se debe ejecutar desde la carpeta raiz para su correcto funcionamiento

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
/root/
├── README.md
├── src/
│   ├── main.py
│   ├── calculations/
│   │   ├── __init__.py
│   │   ├── mortgage_calculator.py
│   │   └── report_generator.py
│   ├── ui/
│   │   ├── __init__.py
│   │   ├── web_interface.py
│   │   └── cli_interface.py
│   └── utils/
│       ├── __init__.py
│       ├── data_validation.py
│       └── file_exporter.py
├── tests/
│   ├── test_calculations.py
│   ├── test_ui.py
│   └── test_utils.py
├── requirements.txt
├── .gitignore
└── docs/
    ├── project_documentation.md
    └── api_reference.md
```

### Instrucciones para Pruebas Unitarias

1. Configura un framework de pruebas con `unittest`
2. Crea archivos de prueba separados, como `test_<nombre_del_módulo>.py`.
3. Ejecuta las pruebas con herramientas `python -m unittest`.


### Descripción de Carpetas y Archivos

- **src/**: Contiene el código fuente del proyecto.
  - **main.py**: Archivo principal para ejecutar la aplicación.
  - **calculations/**: Módulo para cálculos financieros y generación de reportes.
  - **ui/**: Módulo para la interfaz de usuario, ya sea web o CLI.
  - **utils/**: Utilidades generales como validación de datos y exportación de archivos.

- **tests/**: Contiene los archivos de pruebas unitarias para los diferentes módulos.

- **requirements.txt**: Lista de dependencias del proyecto.

- **.gitignore**: Archivo para especificar qué archivos o carpetas deben ser ignorados por Git.

- **docs/**: Documentación adicional del proyecto, como especificaciones y referencias de la API.


## Casos de Estudio

Los casos específicos para el análisis del proyecto se encuentran en el siguiente enlace de Google Sheets:

https://docs.google.com/spreadsheets/d/13gb_k_L8XEZlQfSJO_waRds3wgISHP0f5UH5qSc5wlM/edit?usp=sharing

## Artículo sobre Hipoteca Inversa - Universidad de Medellín
https://repository.udem.edu.co/bitstream/handle/11407/6356/T_MF_436.pdf?sequence=2&isAllowed=y

## Equipo de Trabajo

- Nombre del docente: William David Velásquez

- Integrantes del equipo: Emanuel García Rios y Juan José Becerra

## Tecnologías Utilizadas

- Lenguaje de Programación: Python X

- Frameworks: Django / Flask (según preferencia) X

- Base de Datos: SQLite X

- Bibliotecas para cálculos financieros: NumPy, Pandas

- Generación de gráficos: Matplotlib, Seaborn
