# Proyecto QA para Urban Grocers

## Descripción del Proyecto

Este proyecto está diseñado para automatizar las pruebas de la funcionalidad de creación y gestión de kits en la aplicación Urban Grocers. Las pruebas incluyen la creación, búsqueda, actualización y eliminación de kits, así como la validación de diversos parámetros y escenarios para asegurar el correcto funcionamiento de la API de kits. El objetivo es garantizar que el sistema maneje correctamente las solicitudes y respuestas para diferentes configuraciones de entrada.

## Documentación

La fuente de documentación para este proyecto es la documentación de la API proporcionada por Urban Grocers. La documentación está disponible en [este enlace](https://cnt-20101313-09fa-4b33-af22-1c5354ef1d53.containerhub.tripleten-services.com/docs/), la cual se ha utilizado para entender las rutas de la API y los parámetros necesarios para las solicitudes.

## Tecnologías y Técnicas Utilizadas

- **Python**: El lenguaje de programación principal utilizado para implementar las pruebas automatizadas.
- **Pytest**: Framework de pruebas para realizar pruebas unitarias y de integración en Python.
- **Requests**: Biblioteca utilizada para hacer solicitudes HTTP a la API.
- **Git y GitHub**: Herramientas de control de versiones y colaboración para gestionar el código y el proyecto.
- **TripleTen**: Plataforma utilizada para enlazar el proyecto con GitHub y gestionar el entorno de pruebas.

## Funcionalidades Implementadas

- **Generación de Token**: Función para crear un nuevo usuario y obtener el token de autenticación necesario para realizar solicitudes de API.
- **Creación de Kits**: Función para crear nuevos kits utilizando el token de autenticación.
- **Obtención de Kits**: Función para recuperar y verificar la información de un kit específico.
- **Búsqueda de Kits**: Función para buscar kits por parámetros específicos.
- **Eliminación de Kits**: Función para eliminar kits de la base de datos.
- **Actualización de Kits**: Función para actualizar la información de un kit existente.

## Instrucciones para Ejecutar las Pruebas

1. **Configuración del Entorno**: Asegúrate de tener Python y Pytest instalados en tu entorno de desarrollo.
2. **Clonación del Repositorio**: Clona el repositorio en tu máquina local usando `git clone <URL del repositorio>`.
3. **Ejecutar Pruebas**: Navega al directorio del proyecto y ejecuta las pruebas usando el comando `pytest`.
