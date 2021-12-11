from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name = "Titulo")
    description = models.TextField(verbose_name = "Descripción")
    image = models.ImageField(verbose_name = "Imagen", upload_to = "project")
    link = models.URLField(null = True, blank=True,verbose_name="URLS")
    created = models.DateTimeField(auto_now_add=True, verbose_name = "Fecha De Creación") 
    updated = models.DateTimeField(auto_now=True, verbose_name ="Fecha De Edición")

    class Meta:
        verbose_name = 'proyecto'
        verbose_name_plural = 'proyectos'
        ordering = ["-created"]

    def __str__(Self):
        return Self.title
 
