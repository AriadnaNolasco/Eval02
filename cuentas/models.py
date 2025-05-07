from django.db import models
from django.contrib.auth import get_user_model  # Para obtener el modelo de usuario personalizado o el estándar
# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)  # Permite descripciones opcionales

    class Meta:
        verbose_name_plural = "Categorias"  # Corrige el plural en español

    def __str__(self):
        return self.nombre
    

class Transaccion(models.Model):
    usuario = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='transacciones')
    tipo = models.CharField(max_length=1, choices=[('I', 'Ingreso'), ('G', 'Gasto')])
    monto = models.DecimalField(max_digits=10, decimal_places=2)  # Almacena valores monetarios con precisión
    fecha = models.DateField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='transacciones')
    descripcion = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ['-fecha']  # Ordena las transacciones por fecha descendente

    def __str__(self):
        return f"{self.tipo} - {self.monto} ({self.fecha})"