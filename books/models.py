from django.db import models
from abc import abstractmethod



class BaseEntidad(models.Model):
    """
    Clase abstracta que representa una entidad base con campos comunes
    - titulo (str): Titulo del libro
    - fecha_creacion (datetime): Fecha de creacion del libro
    - fecha_modificacion (datetime): Fecha de modificacion del libro
    """

    titulo = models.CharField(max_length=255)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ['-published_date']

    def __str__(self) -> str:
        return self.title

    @abstractmethod
    def get_info(self) -> str:
        'Metodo polimorfico que devuelve la informacion del libro'
        pass


class Autor(models.Model):
    """
    Clase que representa un autor de libros
    - nombre (str): Nombre del Autor
    - apellido (str): Apellido del autor
    - fecha_nacimiento (date): Fecha de nacimiento del autor
    - nacionalidad (str): Nacionalidad del autor
    - sitio_web (url): Sitio web del autor
    """

    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    nacionalidad = models.CharField(max_length=100)
    sitio_web = models.URLField(blank=True, null=True)

    class Meta:
        ordering = ['apellido', 'nombre']

    def __str__(self) -> str:
        return f"{self.nombre} {self.apellido}".strip()


class Genero(models.Model):
    """
    Clase que representa un tipo de genero
    - nombre (str): Nombre del genero
    """
    nombre = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ['nombre']

    def __str__(self) -> str:
        return self.nombre
