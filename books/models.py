from django.db import models
from django.utils import timezone
from decimal import Decimal, InvalidOperation


class BaseEntidad(models.Model):
    """
    Clase abstracta que representa una entidad base con campos comunes
    - titulo (str): Titulo del libro
    - fecha_creacion (datetime): Fecha de creacion del libro
    - fecha_modificacion (datetime): Fecha de modificacion del libro
    """

    titulo = models.CharField(
            "Título",
            max_length=255,
            db_index=True,
            blank=True,
            default = ""
            )

    fecha_creacion = models.DateTimeField(
            "Fecha de creación",
            default = timezone.now,
            editable=False
            )

    fecha_modificacion = models.DateTimeField(
            "Fecha de modificación",
            auto_now=True,
            editable=False
            )

    class Meta:
        abstract = True
        ordering = ['-fecha_creacion']

    def __str__(self) -> str:
        return self.titulo

    def get_info(self):
        'Metodo polimorfico que devuelve la informacion del libro'
        raise NotImplementedError("Es obligatorio que se implemente este metodo en las subclases")


class Autor(BaseEntidad):
    """
    Clase que representa un autor de libros
    - nombre (str): Nombre del Autor
    - apellido (str): Apellido del autor
    - fecha_nacimiento (date): Fecha de nacimiento del autor
    - nacionalidad (str): Nacionalidad del autor
    - sitio_web (url): Sitio web del autor
    """

    nombre = models.CharField(
            "Nombre",
            max_length=100,
            db_index=True
            )

    apellido = models.CharField(
            "Apellido",
            max_length=100,
            db_index=True
            )

    fecha_nacimiento = models.DateField(
            "Fecha de nacimiento",
            blank=True,
            null=True
            )

    nacionalidad = models.CharField(
            "Nacionalidad",
            max_length=100,
            blank=True,
            null=True
            )

    sitio_web = models.URLField(
            "Sitio web",
            blank=True,
            null=True
            )

    @property
    def nombre_completo(self) -> str:
        'Devuelve el nombre completo del autor'
        return f"{self.nombre} {self.apellido}".strip()

    def __str__(self) -> str:
        return self.nombre_completo

    def save(self, *args, **kwargs) -> None:
        """ Sobrescribe el metodo save para actualizar el titulo con el nombre completo """
        self.titulo = self.nombre_completo
        super().save(*args, **kwargs)

    def get_info(self) -> str:
        fnac = self.fecha_nacimiento.isoformat() if self.fecha_nacimiento else "N/D"
        nac = self.nacionalidad or "N/D"

        return f"{self.nombre_completo}, nacido el {fnac}, Nacionalidad: {nac}"

    class Meta:
        ordering = ["apellido", "nombre"]
        verbose_name = "Autor"
        verbose_name_plural = "Autores"

        constraints = [
            models.UniqueConstraint(
                fields=["nombre", "apellido", "fecha_nacimiento"],
                name="uq_autor_nombre_apellido_fnac"
            )
        ]


class Genero(BaseEntidad):
    """
    Clase que representa un tipo de genero
    - nombre (str): Nombre del genero
    """

    nombre = models.CharField(
            "Nombre",
            max_length=100,
            unique=True,
            db_index=True
            )

    def __str__(self) -> str:
        return self.nombre

    def save(self, *args, **kwargs):
        """ Sobrescribe el metodo save para actualizar el titulo con el nombre del género """
        self.titulo = self.nombre
        super().save(*args, **kwargs)

    def get_info(self) -> str:
        return f"Género: {self.nombre}"

    class Meta:
        ordering = ["nombre"]
        verbose_name = "Género"
        verbose_name_plural = "Géneros"


class Libro(BaseEntidad):
    """
    Clase que representa un libro
    - titulo (str): Titulo del libro
    - autor (Autor): Autor del libro
    - genero (Genero): Género(s) del libro
    - isbn (str): ISBN del libro
    - publicado (date): Fecha de publicación del libro
    - precio (Decimal): Precio del libro
    - stock (int): Stock disponible del libro
    """

    autor = models.ForeignKey(
            "Autor",
            on_delete = models.CASCADE,
            related_name="libros",
            verbose_name="Autor"
            )

    generos = models.ManyToManyField(
            "Genero",
            related_name = "libros",
            verbose_name = "Géneros"
            )

    isbn = models.CharField(
            "ISBN",
            max_length=13,
            unique=True
            )

    publicado = models.DateField(
            "Fecha de publicación",
            null=True,
            blank=True
            )

    _precio = models.DecimalField(
            "Precio (€)",
            max_digits=8,
            decimal_places=2,
            db_column="precio"
            )

    _stock = models.PositiveIntegerField(
            "Stock",
            default=0,
            db_column="stock"
            )

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, value):
        try:
            v = Decimal(str(value))
        except (InvalidOperation, TypeError, ValueError):
            raise ValueError("El precio debe ser numérico (Decimal).")

        if v < 0:
            raise ValueError("El precio no puede ser negativo.")
        self._precio = v

    @property
    def stock(self) -> int:
        return self._stock

    @stock.setter
    def stock(self, value) -> None:
        try:
            v = int(value)
        except (TypeError, ValueError):
            raise ValueError("El stock debe ser un entero.")

        if v < 0:
            raise ValueError("El stock no puede ser negativo.")
        self._stock = v

    def __str__(self):
        return f"{self.titulo} — {self.autor}"

    def get_info(self) -> str:
        precio_txt = f"{self.precio:.2f}€" if self.precio is not None else "N/D"
        pub_txt = self.publicado.isoformat() if self.publicado else "N/D"

        return f"'{self.titulo}' de {self.autor} · ISBN {self.isbn} · {precio_txt} · Publicado: {pub_txt}"

    class Meta(BaseEntidad.Meta):
        ordering = ["titulo"]


class DetalleLibro(models.Model):
    """
    Clase que representa los detalles adicionales de un libro
    - libro (Libro): Libro al que pertenecen los detalles
    - resumen (str): Resumen del libro
    - num_paginas (int): Número de páginas del libro
    """

    libro = models.OneToOneField(
            Libro,
            on_delete=models.CASCADE,
            related_name="detalle"
            )

    resumen = models.TextField(
            "Resumen",
            blank=True,
            null=True
            )

    num_paginas = models.PositiveIntegerField(
            "Número de páginas",
            default=0
            )

    def __str__(self):
        return f"Detalles de {self.libro.titulo}"

