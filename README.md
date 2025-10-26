# 65EP2405

## Examen Practico UF2405

---

## 1. Modelos y POO:

### Requisitos:

Crea una clase base abstracta (BaseEntidad) que defina atributos comunes: - Nombre o titulo - fecha_creacion - fecha_modificacion

Haz que el modelo principal (Coche, Libro o Empleado) herede de _BaseEntidad_

Aplica encapsulamiento en al menos dos atributos (usando @property y @setter).
Implementa **str**() y un método polimórfico, por ejemplo: - calcular_descuento(), mostrar_info(), evaluar_rendimiento(), etc.

Registra el modelo en el admin con list_display y list_filter.
Crea relaciones:
1 a 1 (ej. User ↔ ProfileUser)
1 a N
N a M si el esquema lo requiere.
