>FASTAPI 

Este es un proyecto de práctica desarrollado con FastAPI para la gestión de usuarios, integrando una base de datos Mysql a través de XAMPP


>Tecnologías Utilizadas

   - Python
   - FastAPI: Framework web moderno y rápido.
   - MySQL: Sistema de gestión de bases de datos (vía XAMPP).
   - Uvicorn: Servidor ASGI para ejecutar la aplicación.
   - Pydantic: Validación de datos mediante modelos.
   - mysql-connector-python: Driver para la conexión con MySQL.


>Requisitos Previos

   - Python 3.10+
   - Entorno virtual activo
   - Dependencias: FastAPI, Uvicorn, Pytest
   - XAMPP (Activar Apache y MySQL)


>Instalación y Configuración

  1. Clonar el repositorio
        git clone https://github.com/Mitzy521/FastAPI_MySQL_XAMPP.git
        cd calculator.api

  2. Crear y activar el entorno virtual
       :Windows
       python -m venv venv
       venv\Scripts\activate

  3. Instalar dependencias
       pip install -r requierements.txt

  4. Configurar la base de datos
       Abre XAMPP y activa los modulos (Apache, MySQL)
       Abre en el buscador http://localhost/phpmyadmin
       Crea una base de datos llamada "fastapi_python"
       
  5. Ejecutar la API
       uvicorn app.main:app --reload


>Endopoints

     Método-------Endpoint----------Descripción 
    - Get        /users           Obtiene la lista de todos los usuarios.
    - POST       /users           Crea un nuevo usuario.
    - GET        /users/{id}      Obtiene un usuario específico por su ID.
    - PUT        /users/{id}      Actualiza los datos de un usuario.
    - DELETE     /users/{id}      Elimina un usuario.


>Mitzy Yuridia Cu Chén
