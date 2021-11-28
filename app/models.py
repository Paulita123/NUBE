from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import PROTECT

import app

User._meta.get_field('email')._unique = True

# Create your models here.
class Partido(models.Model):
    nombre = models.CharField(max_length = 45, null = False)
    visitas = models.IntegerField(default = 0)
    user = models.ForeignKey(
        User,
        related_name = 'partidos',
        null = False,
        on_delete = models.PROTECT
    )
    fecha_creacion = models.DateTimeField(auto_now_add = True)

    class Meta:
        app_label: 'app'

class Individuo(models.Model):
    apellidos = models.CharField(max_length = 45, null = False)
    nombres = models.CharField(max_length = 45, null = False)
    fecha_nacimiento = models.DateField()
    aprobado = models.BooleanField(default = False)
    visitas = models.IntegerField(default = 0)
    fecha_creacion = models.DateTimeField(auto_now_add = True)
    user = models.ForeignKey(
        User,
        related_name = 'individuos',
        null = False,
        on_delete = models.PROTECT
    )
    
    class Meta:
        app_label: 'app'

class Proceso(models.Model):
    titulo = models.CharField(max_length = 45, null = False)
    fecha_inicio = models.DateTimeField(null = False)
    fecha_fin = models.DateTimeField()
    abierto = models.BooleanField(default = False, null = False)
    entidad = models.CharField(max_length = 45, null = False)
    monto = models.IntegerField(default = 0)
    comentarios = models.CharField(max_length = 45)
    aprobado = models.BooleanField(default = False)
    visitas = models.IntegerField(default = 0)
    user = models.ForeignKey(
        User,
        related_name = 'procesos',
        null = False,
        on_delete = models.PROTECT
    )

    class Meta:
        app_label: 'app'

class Afiliacion(models.Model):
    fecha_ingreso = models.DateTimeField()
    fecha_salida = models.DateTimeField()
    aprobado = models.BooleanField(default = False)
    individuo = models.ForeignKey(
        Individuo,
        related_name = 'individuos',
        null = False,
        on_delete = models.PROTECT
    )
    partido = models.ForeignKey(
        Partido,
        related_name = 'partidos',
        null = False,
        on_delete = models.PROTECT
    )

    class Meta:
        app_label: 'app'

class Implicado(models.Model):
    fecha = models.DateTimeField()
    acusacion = models.CharField(max_length = 45)
    culpable = models.BooleanField(default = False)
    pena = models.CharField(max_length = 45)
    comentarios = models.CharField(max_length = 45)
    afiliado = models.ForeignKey(
        Afiliacion,
        related_name = 'afiliados',
        null = False,
        on_delete = models.PROTECT
    )
    proceso = models.ForeignKey(
        Proceso,
        related_name = 'procesos',
        null = False,
        on_delete = models.PROTECT
    )

    class Meta:
        app_label: 'app'