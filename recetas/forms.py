from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Row, Column

from .models import Receta, MedicamentosReceta


class RecetaForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit("submit", "Guardar receta"))

    class Meta:
        model = Receta
        fields = ["paciente"]


class MedicamentoRecetaForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        # self.helper.layout = 

    class Meta:
        model = MedicamentosReceta
        fields = ["medicamento", "cada", "periodicidad_cada", "por", "periodicidad_por"]
