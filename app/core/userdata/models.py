from django.db import models
from django.conf import settings
#from ckeditor.fields import RichTextfield
from .genero import Generos
# Create your models here.
# crear la estroctura en el modelo de datos

class Roles(models.Model):
    roleName=models.CharField(max_length=50)
    

    class Meta:
        verbose_name="Perfile de usuario"
        verbose_name_plural="Perfiles"

    #creo la funcion para llamar atributos
    def __str__(self):
        return self.roleName

class DatosUser(models.Model):
    userDNI = models.CharField(max_length=20,verbose_name="Identificacion")
    NombUser=models.CharField(max_length=200,null=True,verbose_name="Nombre")
    apelUser=models.CharField(max_length=200,null=True,verbose_name="Apellido")
    profeUser=models.CharField(max_length=100,null=True,verbose_name="Profecion")
    fotoUser = models.ImageField(default='user.png', verbose_name = "Foto de perfil", upload_to="perfiles/img")
    teleUser = models.CharField(max_length=20,verbose_name="Numero de telefono") 
    geneUser=models.CharField(max_length=20,choices=Generos, default="Otro",verbose_name="Genero")
    adddata=models.DateTimeField(auto_now_add=True, null=True)
    modifiat=models.DateTimeField(auto_now=True,null=True)


    class Meta:
        verbose_name="Datos del usuario"
        verbose_name_plural="Infomacion"
       

    # definimos la funcion 
    def __str__(self):
        return self.userDNI



class HabilUser(models.Model):
    NombHabi=models.CharField(max_length=100)
    Deschabil=models.TextField(max_length=2000,verbose_name="descrpcion de la habiliadad")
    Prof=models.CharField(max_length=100,verbose_name="Profesion")
    # definimos la funcion 
    class Meta:
        verbose_name="habilidades de usuario"
        verbose_name_plural="Habilidades"

    def __str__(self):
        return self.NombHabi

#agregamos los modelos 

class DetaRoles(models.Model):
    idRole=models.ForeignKey(Roles,on_delete=models.CASCADE,verbose_name="identificador de rol")
    idUser=models.ForeignKey(DatosUser,on_delete=models.CASCADE)
    addUser=models.DateTimeField(auto_now_add=True,auto_now=False)
    udtuser=models.DateTimeField(auto_now=True)
    estaRol=models.CharField(max_length=10)

    class Meta:
        verbose_name="roles  del usuario"
        verbose_name_plural="Roles"
    #funcion de mostrar
    def __str__(self):
        return self.idUser


class Rates(models.Model):
    idRole=models.ForeignKey(Roles,on_delete=models.CASCADE,verbose_name="identificador de rol")
    idUser=models.ForeignKey(DatosUser,on_delete=models.CASCADE)
    psrHabil=models.DecimalField(max_digits=2,decimal_places=1)
    udtHabil=models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name="Nivel de habilidades "
        verbose_name_plural="porcentajes"

     # definimos la funcion 
    def __str__(self):
        return self.idUser


    
