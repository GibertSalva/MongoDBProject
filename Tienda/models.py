from django.db import models

# Create your models here.

class Videojuego(models.Model):
    publicadora_id = models.CharField(max_length=100)
    game_id = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    tipo_juego = models.CharField(max_length=100)
    release_date = models.CharField(max_length=100)
    Espacio = models.CharField(max_length=100)

    def __str__(self):
        return str(self.nombre)

    class Meta:
        abstract = False

class Inventario(models.Model):
    inventario_id = models.CharField(max_length=100)
    pelicula_id = models.CharField(max_length=100)
    tienda_id = models.CharField(max_length=100)

    def __str__(self):
        return str(self.inventario_id)

    class Meta:
        abstract = True

class Rental (models.Model):
    rental_id = models.CharField(max_length=100)
    fecha_renta = models.CharField(max_length=100)
    fecha_de_devolucion = models.CharField(max_length=100)
    inventario_id = models.CharField(max_length=100)
    cliente_id = models.CharField(max_length=100)

    def __str__(self):
        return str(self.rental_id)
    
    class Meta:
        abstract = True

class Publicadora (models.Model):
    publicadora_id = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    Rating = models.CharField(max_length=100)

    def __str__(self):
        return str(self.nombre)
    
    class Meta:
        abstract = True

class Tienda (models.Model):
    nombre = models.CharField(max_length=100)
    url = models.CharField(max_length=100)
    tienda_id = models.CharField(max_length=100)

    def __str__(self):
        return str(self.nombre)
    
    class Meta:
        abstract = True

class Cliente (models.Model):
    cliente_id = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    telefono = models.CharField(max_length=100)
    fecha_nacimiento = models.CharField(max_length=100)
    dni = models.CharField(max_length=100)

    def __str__(self):
        return str(self.nombre)
    
    class Meta:
        abstract = False
