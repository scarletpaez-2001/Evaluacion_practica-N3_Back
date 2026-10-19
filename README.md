Sistema para gestiondes de solicitudes de Soporte Técnico usando API RESTful

Para clonar el repositorio: 
https://github.com/scarletpaez-2001/Evaluacion_practica-N3_Back.git

En esta sección se creó un entorno virtual: python -m venv venv
Activación de entorno virtual: venv\Scripts\activate

Instalación de dependecias: 
pip install -r requirements.txt 

Aplicación de las migraciones a la base de datos:
python manage.py migrate

Creación de superusuario: 
python manage.py createsuperuser

Ejecución del servidor:
python manage.py runserver
para acceder: http://127.0.0.1:8000/api/

Administrador: 
usuario: america
contraseña: scarlet2001
http://127.0.0.1:8000/admin/

Usuario normal: marcia 

Se desarrolla el conjunto de Pruebas Endpoints para:
Listar solicitudes mediante GET  
Crear solicitudes con POST       
Actualizar Solicitud con PUT/PATCH  
Eliminación de solicitud con DELETE 
Solicitudes: http://127.0.0.1:8000/api/solicitudes/
Login: http://127.0.0.1:8000/api-auth/login/


Usé Inteligencia Artificial como guía para el desarrollo los Endpoints, para la validación de métodos, los permisos personalizados, también para apoyarme con la lógica del modelo.
A partir de la asesoriía entregada por la IA, seleccionédos recomendaciones de seguridad aplicables en el proyecto:
Inyección de datos a nivel de servidor
Control de permisos a nivel de objeto 

 Implementación y verificación en el proyecto
Estas recomendaciones fueron aplicadas y verificadas técnicamente en la arquitectura del proyecto:
En serializers.py: Se configuraron los campos sensibles (usuario y fecha_creacion) con la propiedad read_only=True para bloquear cualquier intento de modificación maliciosa desde el cliente de la API.
En views.py: Se sobrescribió el método perform_create para asociar automáticamente el recurso al usuario de la sesión activa serializer.save(usuario=self.request.user), y se implementó una lógica de validación estricta en perform_update y get_queryset para filtrar el acceso a los datos y proteger el cambio de estados en las solicitudes según el perfil.
En permissions.py: Se validaron las clases personalizadas para impedir que usuarios no autorizados ejecuten acciones de borrado de datos.

