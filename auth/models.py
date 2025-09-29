from django.conf import settings
from django.db import models
from recetas.models import ModeloBase, NombreMixin


class Perfil(ModeloBase):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    curp = models.CharField(max_length=18, null=False, blank=False)

    def __str__(self):
        return f"{self.user.name} {self.user.last_name}"


class PerfilDoctor(ModeloBase):
    perfil = models.OneToOneField(Perfil, on_delete=models.CASCADE)
    cedula_profesional = models.CharField(
        max_length=30, null=False, blank=False, verbose_name="Cédula profesional"
    )

    def __str__(self):
        return self.cedula_profesional


class Empresa(ModeloBase, NombreMixin):

    def __str__(self):
        return self.nombre
    
class PerfilFarmacuetico(ModeloBase):
    perfil = models.OneToOneField(Perfil, on_delete=models.CASCADE)
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT)
