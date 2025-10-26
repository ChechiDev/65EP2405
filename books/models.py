from django.db import models
from abc import abstractmethod



class BaseEntidad(models.Model):
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


