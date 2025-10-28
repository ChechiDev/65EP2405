from django.contrib import admin
from .models import Autor, Genero, Libro, DetalleLibro

class DetalleLibroInline(admin.StackedInline):
    model = DetalleLibro
    extra = 0

@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ("nombre", "apellido", "fecha_nacimiento", "nacionalidad", "sitio_web", "fecha_creacion")
    list_filter = ("nacionalidad", "fecha_creacion")
    search_fields = ("nombre", "apellido")
    ordering = ("apellido", "nombre")

@admin.register(Genero)
class GeneroAdmin(admin.ModelAdmin):
    list_display = ("nombre", "fecha_creacion")
    search_fields = ("nombre",)
    ordering = ("nombre",)

@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ("titulo", "autor", "isbn", "precio", "stock", "publicado", "fecha_creacion")
    list_filter = ("publicado", "generos", "fecha_creacion")
    search_fields = ("titulo", "isbn", "autor__nombre", "autor__apellido")
    inlines = [DetalleLibroInline]

    def get_queryset(self, request):
      qs = super().get_queryset(request)
      return qs.select_related("autor").prefetch_related("generos")
