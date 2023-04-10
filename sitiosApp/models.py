import uuid

from django.db import models

def generate_primary_key():
    return uuid.uuid4().hex

class Base(models.Model):
    id = models.CharField(max_length=32, primary_key=True, unique=True, default=generate_primary_key, editable=False, verbose_name='Id')
    
    class Meta:
        abstract = True
        
class BaseName(Base):
    nombre = models.CharField(max_length=25, unique=True, blank=False, verbose_name='Nombre')
    
    class Meta:
        abstract = True
        ordering = ('nombre',)

class TipoSitio(BaseName):
    
    def __str__(self):
        return self.nombre
    
class Provincia(Base):
    codigo = models.CharField(max_length=5, unique=True, blank=False, verbose_name='Código')
    nombre = models.CharField(max_length=25, unique=True, blank=False, verbose_name='Nombre')
    
    class Meta:
        abstract = False
        ordering = ('codigo',)
    
    def __str__(self):
        return self.nombre
    
class Sitio(BaseName):
    direccion = models.CharField(max_length=100, blank=True, verbose_name='Dirección')
    capacidad = models.IntegerField(default=0, verbose_name='Capacidad')
    fechaApertura = models.DateField(verbose_name='Fecha Apertura', help_text = "Por favor use el formato: <em>MM/DD/YYYY</em>.")
    disponible = models.BooleanField(verbose_name='Disponible', default=True)
    foto = models.ImageField(upload_to='sitiosMedia', max_length=255, blank=True, verbose_name='Foto')
    tipo = models.ForeignKey(TipoSitio, on_delete=models.CASCADE, null=False, verbose_name='Tipo')
    provincia = models.ForeignKey(Provincia, on_delete=models.CASCADE, null=False, verbose_name='Provincia')

    def __str__(self):
        return self.nombre
