from django.db import models
from django.conf import settings
from ckeditor.fields import RichTextField
#imporatar modelos de otras app
from userdata.models import DatosUser
# Create your models here.


class TipoDocu(models.Model):
    NombDoc=models.CharField(max_length=200,null=True,verbose_name="tipo de documento")
    

    class Meta:
        verbose_name="tipo de documento"
        verbose_name_plural="Tipo de Documento"

    #creo la funcion para llamar atributos
    def __str__(self):
        return self.NombDoc


class CategProye(models.Model):
    lenguaje=models.CharField(max_length=200,null=True,verbose_name="leguaje de progamacion")
    motorDB=models.CharField(max_length=200,null=True,verbose_name="nombre de la base de datos")
    arquitectura=models.CharField(max_length=200,null=True,verbose_name="tipo de arquitectura de software")

    class Meta:
        verbose_name="categoria del proyecto"
        verbose_name_plural="Categoria"

    #creo la funcion para llamar atributos
    def __str__(self):
        return self.lenguaje


class Proyectos(models.Model):
    idCategProye=models.ForeignKey(CategProye,on_delete=models.CASCADE,verbose_name="identificador de Categoria")
    nombProy=models.CharField(max_length=200,null=True,verbose_name="nombre del proyecto")
    descProy=models.CharField(max_length=200,null=True,verbose_name="descripcion del proyecto")
    imgProy = models.ImageField(default='proyecto.png', upload_to="img/perfiles", verbose_name="Foto del Proyecto")
    fechaIni=models.DateField(auto_now_add=True, null=True,verbose_name="fecha de inicio")
    fechaFin=models.DateField(auto_now_add=True, null=True,verbose_name="fecha fin")
    urlRepo=models.TextField(max_length=200,verbose_name="link del proyecto")
    estaProy=models.CharField(max_length=45,verbose_name="Estado del proyecto")


    class Meta:
        verbose_name="tipo de proyectos"
        verbose_name_plural="Proyectos"

    #creo la funcion para llamar atributos
    def __str__(self):
        return self.nombProy


class documentos(models.Model):
    idTipoDocu=models.ForeignKey(TipoDocu,on_delete=models.CASCADE,verbose_name="identificador de tipo de documento")
    idProyectos=models.ForeignKey(Proyectos,on_delete=models.CASCADE,verbose_name="identificador de la tabla proyectos")
    idUsuario=models.ForeignKey(DatosUser,on_delete=models.CASCADE,verbose_name="identificador de la tabla Usuarios")
    nombDocu=models.CharField(max_length=200,verbose_name="nombre del documento")
    pathDocu=models.FileField(max_length=45,upload_to=None,verbose_name="ruta del documento")

    class Meta:
        verbose_name="documento"
        verbose_name_plural="Documento"

    #creo la funcion para llamar atributos
    def __str__(self):
        return self.nombDocu

    


