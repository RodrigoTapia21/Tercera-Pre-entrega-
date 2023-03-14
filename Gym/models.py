from django.db import models

class Bebida(models.Model):
        nombre_bebida= models.CharField(max_length=20)
        precio_bebida= models.IntegerField()
        marca_bebida= models.CharField(max_length=20)
        litros_bebida=  models.IntegerField()
        
        def __str__(self):
            return f"{self.id} - nombre:{self.nombre_bebida} - ${self.precio_bebida}"
        

class Entrenador(models.Model):
        nombre_entrenador= models.CharField(max_length=20)
        clase_entrenador=  models.CharField(max_length=10)
        
        def __str__(self):
            return f"{self.id} - {self.nombre_entrenador} - {self.clase_entrenador}"


class Clase(models.Model):
        nombre_clase= models.CharField(max_length=20)
        precio_clase= models.IntegerField()
        
        
        def __str__(self):
            return f"{self.id} - nombre:{self.nombre_clase} - ${self.precio_clase} "

