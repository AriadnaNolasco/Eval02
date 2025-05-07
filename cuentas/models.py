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
    
class Cuenta(models.Model):
    usuario = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='cuentas')
    nombre = models.CharField(max_length=100)
    saldo = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)  # Saldo actual de la cuenta
    moneda = models.CharField(max_length=3, default='PEN')  # Moneda de la cuenta (ej: USD, EUR)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Cuentas"

    def __str__(self):
        return self.nombre

class Transaccion(models.Model):
    usuario = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='transacciones')
    tipo = models.CharField(max_length=1, choices=[('I', 'Ingreso'), ('G', 'Gasto')])
    monto = models.DecimalField(max_digits=10, decimal_places=2)  # Almacena valores monetarios con precisión
    fecha = models.DateField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='transacciones')
    cuenta = models.ForeignKey(Cuenta, on_delete=models.CASCADE, related_name='transacciones', null=True, blank=True)
    descripcion = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ['-fecha']  # Ordena las transacciones por fecha descendente

    def __str__(self):
        return f"{self.tipo} - {self.monto} ({self.fecha}) en {self.cuenta}"
    

class Presupuesto(models.Model):
    usuario = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='presupuestos')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='presupuestos')
    monto_presupuestado = models.DecimalField(max_digits=10, decimal_places=2)
    periodo_inicio = models.DateField()
    periodo_fin = models.DateField()

    class Meta:
        verbose_name_plural = "Presupuestos"
        unique_together = ('usuario', 'categoria', 'periodo_inicio', 'periodo_fin') # Evita presupuestos duplicados en el mismo periodo

    def __str__(self):
        return f"Presupuesto de {self.categoria} ({self.periodo_inicio} - {self.periodo_fin})"