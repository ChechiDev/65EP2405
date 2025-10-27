# 65EP2405 - Examen Practico UF2405

### 1. Modelos y POO:

### Requisitos:

Crea una clase base abstracta (BaseEntidad) que defina atributos comunes: - Nombre o titulo - fecha_creacion - fecha_modificacion

Haz que el modelo principal (Coche, Libro o Empleado) herede de _BaseEntidad_

Aplica encapsulamiento en al menos dos atributos (usando @property y @setter).

Implementa **str**() y un método polimórfico, por ejemplo: - calcular_descuento(), mostrar_info(), evaluar_rendimiento(), etc.

Registra el modelo en el admin con list_display y list_filter.

Crea relaciones:
    - 1 a 1 (ej. User ↔ ProfileUser)
    - 1 a N
    - N a M si el esquema lo requiere.

### 2. Vistas basadas en función

Crea una Function-Based View (FBV) que liste los registros del modelo principal.

Permite filtrar al menos los de un resultado mediante parámetros GET (por ejemplo, tipo_combustible, genero, departamento).

Aplica herencia de plantillas (base.html con bloques {% block content %} reutilizables).

Demuestra polimorfismo en la presentación (misma lógica para diferentes datos o tipos de entidad).

### 3. Vistas basadas en clase

Implementa un CRUD completo usando Class-Based Views (CBV):
    - ListView,
    - DetailView,
    - CreateView,
    - UpdateView,
    - DeleteView.

Aplica herencia entre vistas, creando una clase base (BaseView) con configuraciones comunes.

Usa el sistema de mensajes (messages.success, messages.error) al crear o editar datos.

Protege las vistas de creación y edición con LoginRequiredMixin.

### 4. URLs y estructura modular (1 punto)

Define una estructura modular de rutas: /libros/

Declara las rutas en urls.py dentro de cada app.

Usa include() en el urls.py principal.

Asigna nombres (name="...") a todas las rutas para uso en plantillas.

Asegúrate de mantener coherencia POO en la organización de vistas y archivos.

### 5. Autenticación y permisos

Configura el sistema de autenticación de Django:
    - Registro (signup)
    - Login (login)
    - Logout (logout)

Protege vistas CRUD con @login_required o LoginRequiredMixin.

Personaliza plantillas de autenticación heredando de base.html.

Muestra el usuario autenticado en el encabezado del sitio.

### 6. Formularios personalizados

Crea un ModelForm o formulario manual en forms.py.

Añade validaciones personalizadas, por ejemplo:
    - precio > 0
    - stock >= 0
    - salario >= 1000

Aplica encapsulamiento: controla el acceso o modificación de los datos del formulario.

Muestra errores y mensajes de éxito visualmente en la plantilla.

### 7. API REST (1.5 puntos)

Crea una API usando Django REST Framework (DRF):
    - Endpoint /api/[modelo]/ con métodos GET y POST.
    - Implementa ModelSerializer.
    - Añade filtros (DjangoFilterBackend), búsqueda (SearchFilter) y ordenación (OrderingFilter).

Usa herencia de clases DRF (ListCreateAPIView, RetrieveUpdateDestroyAPIView).

### 8. Panel de administración

Personaliza el panel de administración:
    - Columnas (list_display)
    - Filtros (list_filter)
    - Búsqueda (search_fields)

Si hay más de un modelo, aplica herencia o reutilización para mantener el mismo formato de administración.

### 9. Presentación y estructura del proyecto

El proyecto debe:

Ejecutarse correctamente con python manage.py runserver.

Incluir documentación (README.md) con:

- Instrucciones de instalación.
- Usuario demo.

Seguir la estructura:

manage.py
/app_elegida/
    models.py
    views.py
    forms.py
    urls.py
    serializers.py
    templates/
/templates/base.html
/locale/
requirements.txt

Código limpio, comentado, y conforme al estilo PEP8.
