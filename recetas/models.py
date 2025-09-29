from django.db import models
from django.conf import settings


class ModeloBase(models.Model):
    fecha_creacion = models.DateTimeField(
        auto_now_add=True,
        editable=False,
        null=True,
        verbose_name="Fecha de creación",
    )
    fecha_actualizacion = models.DateTimeField(
        auto_now=True,
        editable=False,
        null=True,
        verbose_name="Fecha de actualización",
    )

    creado_por = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        null=True,
        related_name="+",
        editable=False,
        default=1,
    )
    actualizado_por = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        null=True,
        related_name="+",
        editable=False,
        default=1,
    )

    class Meta:
        abstract = True

    def created_by_name(self):
        if self.created_by:
            return self.created_by.get_full_name().strip() or self.created_by.username

    def last_updated_by_name(self):
        if self.last_updated_by:
            return (
                self.last_updated_by.get_full_name().strip()
                or self.last_updated_by.username
            )


class NombreMixin(models.Model):
    nombre = models.CharField(max_length=255)

class MedidaUnidadMixin(models.Model):
    medida = models.DecimalField()
    unidad = models.ForeignKey(Unidad, on_delete=models.PROTECT)

class Unidad(ModeloBase, NombreMixin):
    abreviacion = models.CharField(max_length=15, verbose_name="Abreviación")


class Periodicidad(ModeloBase, NombreMixin):
    pass


class Medicamento(ModeloBase):
    nombre_generico = models.CharField(max_length=255, verbose_name="Nombre genérico")
    unidad_predeterminada = models.ForeignKey(Unidad, on_delete=models.PROTECT)


class Laboratorio(ModeloBase, NombreMixin):
    pass


class Marca(ModeloBase, NombreMixin):
    laboratorio = models.ForeignKey(Laboratorio, on_delete=models.PROTECT)


class Presentacion(ModeloBase, MedidaUnidadMixin):
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT)
    piezas = models.IntegerField()
    medida = models.DecimalField()
    unidad = models.ForeignKey(Unidad, on_delete=models.PROTECT)


class Receta(ModeloBase):
    medicamentos = models.ManyToManyField(Medicamento, through="MedicamentosReceta")
    paciente = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)

class MedicamentosReceta(ModeloBase, MedidaUnidadMixin):
    receta = models.ForeignKey(Receta, on_delete=models.PROTECT)
    medicamento = models.ForeignKey(Medicamento, on_delete=models.PROTECT)
    cada = models.PositiveSmallIntegerField()
    periodicidad_cada = models.ForeignKey(Periodicidad, on_delete=models.PROTECT, verbose_name="Periodicidad")
    por = models.PositiveSmallIntegerField()
    periodicidad_por = models.ForeignKey(Periodicidad, on_delete=models.PROTECT, verbose_name="Periodicidad")
    
