from django.db import models


class Cafeteria(models.Model):
    id = models.AutoField(primary_key= True)
    referencia = models.CharField(max_length=30, blank= False, null = False)
    producto = models.CharField(max_length=30, blank= False, null = False)
    marca = models.CharField(max_length=30, blank= False, null = False)
    precio = models.IntegerField()
    image = models.CharField(max_length = 150, blank = False, null = False)
    calorias = models.CharField(max_length = 150, blank = False, null = False)
    fecha_vencimiento = models.CharField(max_length = 150, blank = False, null = False)
    
    
    #"calorias"
    #"azucares"
    #"fecha de vencimiento"
    
    