from django.contrib import admin
from .models import Categoria, Transaccion, Cuenta, Presupuesto

admin.site.register(Categoria)
admin.site.register(Transaccion)
admin.site.register(Cuenta)
admin.site.register(Presupuesto)
